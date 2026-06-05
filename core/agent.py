from __future__ import annotations
import os
import re
from typing import Optional, Generator
import google.generativeai as genai

from core.system_prompt import get_system_prompt_with_context
from rag.pipeline import KarpathyRAGPipeline, detect_career_phase, get_timeline_description, bootstrap_demo_data
from memory.memory_manager import MemoryManager


# ══════════════════════════════════════════════════════════
# GEMINI CONFIGURATION
# ══════════════════════════════════════════════════════════

GEMINI_MODEL = "gemini-2.5-flash"

GENERATION_CONFIG = genai.types.GenerationConfig(
    temperature=0.75,        # Karpathy is thoughtful but not robotic
    top_p=0.95,
    top_k=40,
    max_output_tokens=8192,
)

SAFETY_SETTINGS = [
    {"category": "HARM_CATEGORY_HARASSMENT",        "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH",       "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]


# ══════════════════════════════════════════════════════════
# TIMELINE ROUTER
# ══════════════════════════════════════════════════════════

def route_timeline(query: str) -> tuple[str, str]:
    """
    Classify the query into a career phase and return
    (phase_key, human_readable_description).
    """
    phase = detect_career_phase(query)
    description = get_timeline_description(phase)
    return phase, description


# ══════════════════════════════════════════════════════════
# KARPATHY AGENT
# ══════════════════════════════════════════════════════════

class KarpathyAgent:
    """
    The Digital Twin agent.

    Call flow per user turn:
      1. route_timeline(query)          → career phase + description
      2. rag.retrieve_with_context()    → retrieved chunks + timeline context
      3. memory.process_user_turn()     → STM add + LTM extraction
      4. build full system prompt       → persona + user profile + RAG context
      5. gemini.send_message()          → streaming or sync response
      6. memory.process_model_turn()    → STM add
    """
    def __init__(
        self,
        google_api_key: str, # We will pass a comma-separated string of keys here
        chroma_persist_dir: str = "./data/chromadb",
        profile_path: str = "./data/memory/user_profile.json",
        rag_top_k: int = 5,
        bootstrap_demo: bool = True,
    ):
        self.rag_top_k = rag_top_k
        
        # 1. Split the incoming string into a list of keys
        api_keys = [k.strip() for k in google_api_key.split(",") if k.strip()]
        self.google_api_key = None
        
        # 2. Try each key until one works
        for key in api_keys:
            try:
                print(f"[Agent] Testing API key: {key[:8]}...")
                genai.configure(api_key=key)
                
                # Do a tiny dummy generation to prove the key is active and not rate-limited
                test_model = genai.GenerativeModel("gemini-2.5-flash")
                test_model.generate_content("test")
                
                # If it succeeds, lock it in and break the loop
                self.google_api_key = key
                print("[Agent] ✓ Key accepted!")
                break
            except Exception as e:
                print(f"[Agent] ✗ Key failed: {e}")
                
        if not self.google_api_key:
            raise ValueError("None of the provided API keys were valid or active.")
        
        # ── Configure Gemini ──────────────────────────────
        genai.configure(api_key=google_api_key)

        # Main inference model
        self._inference_model = genai.GenerativeModel(
            model_name=GEMINI_MODEL,
            generation_config=GENERATION_CONFIG,
            safety_settings=SAFETY_SETTINGS,
        )

        # Lightweight extraction model (same model, different config)
        self._extraction_model = genai.GenerativeModel(
            model_name=GEMINI_MODEL,
            generation_config=genai.types.GenerationConfig(
                temperature=0.1,
                max_output_tokens=512,
            ),
        )

        # ── RAG Pipeline ──────────────────────────────────
        self.rag = KarpathyRAGPipeline(
            persist_dir=chroma_persist_dir,
            google_api_key=google_api_key,
        )

        # Bootstrap demo data if collection is empty
        if bootstrap_demo and self.rag.collection.count() == 0:
            print("[Agent] Empty vector DB — bootstrapping demo corpus...")
            bootstrap_demo_data(self.rag)
            stats = self.rag.collection_stats()
            print(f"[Agent] Vector DB ready: {stats['total_chunks']} chunks indexed.")

        # ── Memory Manager ────────────────────────────────
        self.memory = MemoryManager(
            profile_path=profile_path,
            extraction_model=self._extraction_model,
        )

        # ── Active Chat Session ───────────────────────────
        self._chat_session: Optional[genai.ChatSession] = None
        self._init_chat_session()

        print(f"[Agent] Karpathy Twin ready. Model: {GEMINI_MODEL}")

    def _init_chat_session(self, history: Optional[list] = None) -> None:
        """Create or re-create the Gemini chat session."""
        self._chat_session = self._inference_model.start_chat(
            history=history or []
        )

    def _build_full_prompt(
        self,
        user_query: str,
        retrieved_knowledge: str,
        timeline_description: str,
    ) -> str:
        """
        Assemble the complete system prompt with all dynamic context.
        This is prepended as the very first user message to simulate a system turn.
        """
        user_profile = self.memory.get_user_profile_text()
        return get_system_prompt_with_context(
            user_profile=user_profile,
            timeline_context=timeline_description,
            retrieved_knowledge=retrieved_knowledge,
        )

    def chat(self, user_message: str) -> str:
        """
        Synchronous single-turn. Returns complete response string.
        """
        # 1. Timeline routing
        phase, timeline_desc = route_timeline(user_message)

        # 2. RAG retrieval
        retrieved_knowledge, _ = self.rag.retrieve_with_context(
            query=user_message,
            n_results=self.rag_top_k,
            career_phase_filter=phase if phase != "general" else None,
        )

        # 3. Memory: process user turn (STM add + LTM extraction)
        self.memory.process_user_turn(user_message)

        # 4. Build the full context-rich system instruction
        system_instruction = self._build_full_prompt(
            user_query=user_message,
            retrieved_knowledge=retrieved_knowledge,
            timeline_description=timeline_desc,
        )

        # 5. Re-initialize session with updated system prompt + history
        #    (Gemini SDK requires system_instruction at session creation)
        model_with_context = genai.GenerativeModel(
            model_name=GEMINI_MODEL,
            generation_config=GENERATION_CONFIG,
            safety_settings=SAFETY_SETTINGS,
            system_instruction=system_instruction,
        )
        chat_session = model_with_context.start_chat(
            history=self.memory.get_gemini_history()
        )

        # 6. Send message and get response
        response = chat_session.send_message(user_message)
        response_text = response.text

        # 7. Memory: process model turn (STM add)
        self.memory.process_model_turn(response_text)

        return response_text

    def chat_stream(self, user_message: str) -> Generator[str, None, None]:
        """
        Streaming version. Yields text chunks as they arrive.
        Usage:
            for chunk in agent.chat_stream("How does backprop work?"):
                print(chunk, end="", flush=True)
        """
        # 1. Timeline routing
        phase, timeline_desc = route_timeline(user_message)

        # 2. RAG retrieval
        retrieved_knowledge, _ = self.rag.retrieve_with_context(
            query=user_message,
            n_results=self.rag_top_k,
            career_phase_filter=phase if phase != "general" else None,
        )

        # 3. Memory: process user turn
        self.memory.process_user_turn(user_message)

        # 4. Build full system instruction
        system_instruction = self._build_full_prompt(
            user_query=user_message,
            retrieved_knowledge=retrieved_knowledge,
            timeline_description=timeline_desc,
        )

        # 5. Model with updated context
        model_with_context = genai.GenerativeModel(
            model_name=GEMINI_MODEL,
            generation_config=GENERATION_CONFIG,
            safety_settings=SAFETY_SETTINGS,
            system_instruction=system_instruction,
        )
        chat_session = model_with_context.start_chat(
            history=self.memory.get_gemini_history()
        )

        # 6. Stream response
        full_response = ""
        response_stream = chat_session.send_message(user_message, stream=True)
        for chunk in response_stream:
            try:
                # Safely attempt to read the text
                text = chunk.text
                if text:
                    full_response += text
                    yield text
            except ValueError:
                # Silently catch the empty chunk Google sends when generation finishes
                pass

        # 7. Memory: process model turn (after full response collected)
        self.memory.process_model_turn(full_response)

    def reset_session(self) -> None:
        """Clear short-term memory and start a fresh chat session."""
        self.memory.clear_session()
        self._init_chat_session()
        print("[Agent] Session reset. Long-term memory preserved.")

    def get_memory_dashboard(self) -> dict:
        """Return structured memory state for the dashboard."""
        viz = self.memory.get_visualization()
        rag_stats = self.rag.collection_stats()
        return {
            "memory": viz,
            "rag": rag_stats,
            "model": GEMINI_MODEL,
        }

    def get_rag_stats(self) -> dict:
        return self.rag.collection_stats()
