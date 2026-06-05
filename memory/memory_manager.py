"""
SECTION 3: DUAL-LAYER MEMORY SYSTEM

Short-Term Memory:  Session-scoped conversation buffer (in-memory list).
Long-Term Memory:   Persistent user-profile JSON extracted from conversation.

The long-term extractor listens to user messages and uses Gemini to extract
factual claims about the user (goals, background, current projects, struggles).
These facts persist across sessions and are re-injected on startup.
"""

from __future__ import annotations
import json
import time
import hashlib
from pathlib import Path
from dataclasses import dataclass, field, asdict
from typing import Optional
import google.generativeai as genai


# ══════════════════════════════════════════════════════════
# SHORT-TERM MEMORY: Session Buffer
# ══════════════════════════════════════════════════════════

@dataclass
class ChatTurn:
    role: str          # "user" or "model"
    content: str
    timestamp: float = field(default_factory=time.time)

    def to_gemini_format(self) -> dict:
        return {"role": self.role, "parts": [{"text": self.content}]}


class ShortTermMemory:
    """
    In-session conversation buffer. Keeps recent turns for Gemini's history.
    Applies a rolling window to stay within context limits.
    """

    def __init__(self, max_turns: int = 20):
        self.max_turns = max_turns
        self._turns: list[ChatTurn] = []

    def add(self, role: str, content: str) -> None:
        self._turns.append(ChatTurn(role=role, content=content))
        # Rolling window
        if len(self._turns) > self.max_turns * 2:
            # Keep system-critical first turn if present, then trim middle
            self._turns = self._turns[-self.max_turns * 2:]

    def to_gemini_history(self) -> list[dict]:
        """Format for Gemini's `history` parameter in chat sessions."""
        # Gemini requires alternating user/model turns starting with user
        history = []
        for turn in self._turns[:-1]:  # exclude the most recent (it's the current input)
            history.append(turn.to_gemini_format())
        return history

    def get_recent_text(self, n_turns: int = 6) -> str:
        """Plain-text summary of recent conversation for system prompt injection."""
        recent = self._turns[-n_turns * 2:]
        lines = []
        for t in recent:
            prefix = "User" if t.role == "user" else "Karpathy"
            lines.append(f"{prefix}: {t.content[:300]}{'...' if len(t.content) > 300 else ''}")
        return "\n".join(lines)

    def clear(self) -> None:
        self._turns = []

    def __len__(self) -> int:
        return len(self._turns)


# ══════════════════════════════════════════════════════════
# LONG-TERM MEMORY: Persistent User Profile
# ══════════════════════════════════════════════════════════

@dataclass
class UserFact:
    """A single extracted fact about the user."""
    category: str      # "goal", "background", "project", "struggle", "preference", "knowledge_level"
    content: str
    confidence: float  # 0–1
    turn_index: int    # which conversation turn this was extracted from
    timestamp: float = field(default_factory=time.time)
    source_quote: str = ""  # the user's actual words that triggered this fact

    def to_dict(self) -> dict:
        return asdict(self)


class LongTermMemory:
    """
    Persistent user profile stored as JSON.
    On each user message, runs a lightweight Gemini call to extract facts.
    On session start, loads and formats the profile for system prompt injection.
    """

    EXTRACTION_PROMPT = """
You are an information extraction assistant. Given a user's message in a conversation with 
Andrej Karpathy's Digital Twin, extract structured facts about the user.

Focus on:
- Their technical background (ML engineer, student, researcher, etc.)
- Their current project or what they're building
- Their learning goals
- Their struggles or blockers
- Their knowledge level (beginner, intermediate, expert in specific areas)
- Any preferences (e.g., prefers PyTorch over TF, working on edge devices, etc.)

Return ONLY a JSON array of fact objects (empty array [] if nothing new to extract):
[
  {
    "category": "background|goal|project|struggle|preference|knowledge_level",
    "content": "concise factual statement about the user",
    "confidence": 0.0-1.0,
    "source_quote": "the exact phrase or sentence that revealed this"
  }
]

Do NOT extract facts that are already obvious from the question itself (e.g., don't extract 
"user asked about transformers" — that's not a fact about them).
Only extract durable facts about who they are or what they're working on.
"""

    def __init__(
        self,
        profile_path: str = "./data/memory/user_profile.json",
        model_name: str = "gemini-2.5-flash",
    ):
        self.profile_path = Path(profile_path)
        self.profile_path.parent.mkdir(parents=True, exist_ok=True)
        self.model_name = model_name
        self._facts: list[UserFact] = []
        self._turn_counter = 0
        self._load()

    def _load(self) -> None:
        if self.profile_path.exists():
            try:
                data = json.loads(self.profile_path.read_text())
                self._facts = [UserFact(**f) for f in data.get("facts", [])]
                self._turn_counter = data.get("turn_counter", 0)
                print(f"[Memory] Loaded {len(self._facts)} long-term facts from profile.")
            except Exception as e:
                print(f"[Memory] Could not load profile: {e}")
                self._facts = []

    def _save(self) -> None:
        data = {
            "facts": [f.to_dict() for f in self._facts],
            "turn_counter": self._turn_counter,
            "last_updated": time.time(),
        }
        self.profile_path.write_text(json.dumps(data, indent=2))

    def extract_and_store(self, user_message: str, model: genai.GenerativeModel) -> list[UserFact]:
        """
        Run lightweight extraction on a user message.
        Returns list of newly extracted facts.
        Silently skips if extraction fails.
        """
        self._turn_counter += 1

        # Don't run extraction on very short messages
        if len(user_message.strip()) < 20:
            return []

        # Only run extraction every other turn to reduce API calls
        if self._turn_counter % 2 != 0:
            return []

        try:
            response = model.generate_content(
                f"{self.EXTRACTION_PROMPT}\n\nUser message:\n\"{user_message}\""
            )
            raw = response.text.strip()

            # Strip markdown fences if present
            if raw.startswith("```"):
                raw = re.sub(r"```(?:json)?", "", raw).replace("```", "").strip()

            extracted = json.loads(raw)
            new_facts = []

            for item in extracted:
                # Dedup: skip if very similar fact already exists
                if self._is_duplicate(item.get("content", "")):
                    continue
                fact = UserFact(
                    category=item.get("category", "general"),
                    content=item.get("content", ""),
                    confidence=float(item.get("confidence", 0.7)),
                    turn_index=self._turn_counter,
                    source_quote=item.get("source_quote", ""),
                )
                self._facts.append(fact)
                new_facts.append(fact)

            if new_facts:
                self._save()
                print(f"[Memory] Extracted {len(new_facts)} new fact(s) about the user.")

            return new_facts

        except Exception as e:
            # Extraction is non-critical — never crash the main flow
            print(f"[Memory] Extraction skipped: {e}")
            return []

    def _is_duplicate(self, content: str, threshold: float = 0.8) -> bool:
        """Simple word-overlap dedup heuristic."""
        if not content:
            return True
        content_words = set(content.lower().split())
        for existing in self._facts:
            existing_words = set(existing.content.lower().split())
            if not existing_words:
                continue
            overlap = len(content_words & existing_words) / len(content_words | existing_words)
            if overlap > threshold:
                return True
        return False

    def format_for_prompt(self) -> str:
        """Format user profile for injection into system prompt."""
        if not self._facts:
            return "No prior user information on file."

        lines = ["Known facts about this user:"]
        by_category: dict[str, list[UserFact]] = {}
        for fact in self._facts:
            by_category.setdefault(fact.category, []).append(fact)

        category_order = ["background", "knowledge_level", "project", "goal", "struggle", "preference"]
        for cat in category_order:
            facts = by_category.get(cat, [])
            if facts:
                lines.append(f"\n  [{cat.upper()}]")
                for f in facts:
                    conf_star = "★" if f.confidence >= 0.85 else "☆"
                    lines.append(f"    {conf_star} {f.content}")

        return "\n".join(lines)

    def get_visualization_data(self) -> dict:
        """Return structured data for the memory dashboard."""
        return {
            "total_facts": len(self._facts),
            "total_turns": self._turn_counter,
            "by_category": {
                cat: [f.to_dict() for f in facts]
                for cat, facts in self._group_by_category().items()
            },
        }

    def _group_by_category(self) -> dict:
        result: dict[str, list[UserFact]] = {}
        for f in self._facts:
            result.setdefault(f.category, []).append(f)
        return result

    def clear(self) -> None:
        self._facts = []
        self._turn_counter = 0
        self._save()
        print("[Memory] Long-term memory cleared.")

    def add_manual_fact(self, category: str, content: str) -> None:
        """Manually inject a fact (e.g., from user settings)."""
        fact = UserFact(
            category=category,
            content=content,
            confidence=1.0,
            turn_index=0,
        )
        self._facts.append(fact)
        self._save()

    def __len__(self) -> int:
        return len(self._facts)


# ══════════════════════════════════════════════════════════
# COMBINED MEMORY MANAGER
# ══════════════════════════════════════════════════════════

import re  # needed for extraction cleaning


class MemoryManager:
    """
    Convenience wrapper that coordinates both memory layers.
    This is what the app imports and calls.
    """

    def __init__(
        self,
        profile_path: str = "./data/memory/user_profile.json",
        max_short_term_turns: int = 20,
        extraction_model: Optional[genai.GenerativeModel] = None,
    ):
        self.short_term = ShortTermMemory(max_turns=max_short_term_turns)
        self.long_term = LongTermMemory(profile_path=profile_path)
        self._extraction_model = extraction_model

    def set_extraction_model(self, model: genai.GenerativeModel) -> None:
        self._extraction_model = model

    def process_user_turn(self, user_message: str) -> list[UserFact]:
        """Called when user sends a message. Adds to short-term, triggers extraction."""
        self.short_term.add("user", user_message)
        if self._extraction_model:
            return self.long_term.extract_and_store(user_message, self._extraction_model)
        return []

    def process_model_turn(self, model_response: str) -> None:
        """Called when model responds."""
        self.short_term.add("model", model_response)

    def get_gemini_history(self) -> list[dict]:
        return self.short_term.to_gemini_history()

    def get_user_profile_text(self) -> str:
        return self.long_term.format_for_prompt()

    def get_visualization(self) -> dict:
        return {
            "short_term": {
                "turns": len(self.short_term),
                "recent_preview": self.short_term.get_recent_text(n_turns=3),
            },
            "long_term": self.long_term.get_visualization_data(),
        }

    def clear_session(self) -> None:
        """Clear short-term memory only (new session)."""
        self.short_term.clear()

    def clear_all(self) -> None:
        """Nuke everything."""
        self.short_term.clear()
        self.long_term.clear()
