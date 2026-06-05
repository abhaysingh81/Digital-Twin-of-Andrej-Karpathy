"""
SECTION 2: DATA PIPELINE & GROUNDED RAG ENGINE
Code-aware chunking, timeline tagging, and semantic retrieval with ChromaDB.
"""

from __future__ import annotations
import re
import json
import hashlib
from pathlib import Path
from dataclasses import dataclass, field, asdict
from typing import Optional
import chromadb
from chromadb.utils import embedding_functions


# ══════════════════════════════════════════════════════════
# 1. TIMELINE METADATA SCHEMA
# ══════════════════════════════════════════════════════════

CAREER_PHASES = {
    "stanford": {
        "label": "Stanford PhD Era",
        "years": "2011–2015",
        "keywords": ["cs231n", "convnet", "rnn", "lstm", "image captioning",
                     "fei-fei li", "unreasonable effectiveness", "stanford",
                     "convolutional", "object detection", "visualizing"],
        "description": "PhD at Stanford under Fei-Fei Li, built CS231n from scratch."
    },
    "openai_v1": {
        "label": "OpenAI Era (v1)",
        "years": "2015–2017",
        "keywords": ["openai", "reinforcement learning", "policy gradient", "ppo",
                     "generative models", "gan", "variational", "dota", "rl"],
        "description": "Founding research scientist at OpenAI, deep RL and generative models."
    },
    "tesla": {
        "label": "Tesla Autopilot / FSD Era",
        "years": "2017–2022",
        "keywords": ["tesla", "autopilot", "fsd", "full self-driving", "perception",
                     "occupancy", "bev", "bird's eye view", "data engine",
                     "fleet", "annotation", "deployment", "ai day", "hydranet",
                     "lidar", "radar", "camera-only"],
        "description": "Led Tesla's Autopilot vision team — real-world NN deployment at scale."
    },
    "openai_v2": {
        "label": "OpenAI Era (v2) / LLM Era",
        "years": "2022–2023",
        "keywords": ["gpt", "gpt-4", "llm", "large language model", "transformer",
                     "attention", "rlhf", "scaling", "tokenizer", "bpe",
                     "software 2.0", "backpropagation", "makemore", "nanoGPT",
                     "zero to hero", "neural networks zero to hero"],
        "description": "Returned to OpenAI, built nanoGPT, created Neural Networks: Zero to Hero."
    },
    "eureka": {
        "label": "Eureka Labs Era",
        "years": "2024–present",
        "keywords": ["eureka labs", "llm101n", "education", "ai tutor",
                     "personalized learning", "curriculum", "llm101"],
        "description": "Founded Eureka Labs — AI-native education company."
    },
}

from chromadb.api.types import Documents, EmbeddingFunction

class SafeGeminiEmbeddings(EmbeddingFunction):
    """Custom wrapper to bypass ChromaDB's broken ClientOptions headers bug."""
    def __init__(self, api_key: str, model_name: str):
        import google.generativeai as genai
        genai.configure(api_key=api_key)
        self.model_name = model_name

    def __call__(self, input: Documents) -> list[list[float]]:
        import google.generativeai as genai
        # Ask Google to embed the chunk of text
        result = genai.embed_content(
            model=self.model_name,
            content=input,
            task_type="retrieval_document"
        )
        return result['embedding']
    

def detect_career_phase(text: str) -> str:
    """
    Heuristic: scan text for era-specific keywords and return the best matching
    career phase label. Returns 'general' if nothing specific fires.
    """
    text_lower = text.lower()
    scores = {}
    for phase, meta in CAREER_PHASES.items():
        score = sum(1 for kw in meta["keywords"] if kw in text_lower)
        if score > 0:
            scores[phase] = score
    if not scores:
        return "general"
    return max(scores, key=scores.get)


def get_timeline_description(phase: str) -> str:
    if phase in CAREER_PHASES:
        m = CAREER_PHASES[phase]
        return f"{m['label']} ({m['years']}): {m['description']}"
    return "General knowledge / cross-era."


# ══════════════════════════════════════════════════════════
# 2. SOURCE METADATA SCHEMA
# ══════════════════════════════════════════════════════════

@dataclass
class SourceMetadata:
    """Structured metadata attached to every RAG chunk."""
    source_title: str
    source_type: str          # "blog", "youtube", "paper", "lecture", "talk", "book"
    date: str                 # ISO-ish: "2015-05", "2023-11", "2017"
    career_phase: str         # one of CAREER_PHASES keys or "general"
    url: str = ""
    chunk_index: int = 0
    has_code: bool = False
    language: str = "en"
    extra: dict = field(default_factory=dict)

    def to_chroma_meta(self) -> dict:
        """Flatten for ChromaDB (no nested dicts)."""
        return {
            "source_title": self.source_title,
            "source_type": self.source_type,
            "date": self.date,
            "career_phase": self.career_phase,
            "url": self.url,
            "chunk_index": self.chunk_index,
            "has_code": self.has_code,
            "language": self.language,
        }

    def to_citation(self) -> str:
        type_labels = {
            "youtube": "YouTube",
            "blog": "blog post",
            "paper": "paper",
            "lecture": "lecture",
            "talk": "talk/presentation",
            "book": "book",
        }
        label = type_labels.get(self.source_type, self.source_type)
        return f'[Source: "{self.source_title}", {label}, {self.date}]'


# ══════════════════════════════════════════════════════════
# 3. CODE-AWARE MARKDOWN SPLITTER
# ══════════════════════════════════════════════════════════

class KarpathyMarkdownSplitter:
    """
    Splits Markdown/blog content while NEVER cutting inside a code block.

    Strategy:
      1. Parse the document into segments: prose and code fences.
      2. Accumulate prose segments until we hit the chunk_size limit.
      3. Code blocks are NEVER split — they are always kept whole.
         If a code block is larger than max_chunk_size, it becomes its own chunk.
      4. Overlap is applied only on prose segments, not across code block boundaries.
    """

    def __init__(
        self,
        chunk_size: int = 1200,
        chunk_overlap: int = 150,
        max_chunk_size: int = 3000,
    ):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.max_chunk_size = max_chunk_size

        # Matches ```lang ... ``` or ~~~ ... ~~~
        self._code_fence = re.compile(
            r"(```[\w]*\n[\s\S]*?```|~~~[\w]*\n[\s\S]*?~~~)",
            re.MULTILINE
        )

    def _segment(self, text: str) -> list[dict]:
        """Return list of {type: 'prose'|'code', content: str}."""
        segments = []
        last_end = 0
        for m in self._code_fence.finditer(text):
            if m.start() > last_end:
                segments.append({"type": "prose", "content": text[last_end:m.start()]})
            segments.append({"type": "code", "content": m.group(0)})
            last_end = m.end()
        if last_end < len(text):
            segments.append({"type": "prose", "content": text[last_end:]})
        return segments

    def split_text(self, text: str) -> list[str]:
        """Return list of chunks with code blocks kept whole."""
        segments = self._segment(text)
        chunks: list[str] = []
        current_chunk = ""

        for seg in segments:
            content = seg["content"]

            if seg["type"] == "code":
                # If the code block fits in current chunk, append
                if len(current_chunk) + len(content) <= self.max_chunk_size:
                    current_chunk += "\n" + content
                else:
                    # Flush current prose chunk first
                    if current_chunk.strip():
                        chunks.append(current_chunk.strip())
                    # Code block becomes its own chunk (possibly oversized — intentional)
                    chunks.append(content.strip())
                    current_chunk = ""
            else:
                # Prose: split by sentence boundaries when we exceed chunk_size
                sentences = self._split_prose(content)
                for sentence in sentences:
                    if len(current_chunk) + len(sentence) > self.chunk_size:
                        if current_chunk.strip():
                            chunks.append(current_chunk.strip())
                            # Overlap: carry last N chars into next chunk
                            overlap_text = current_chunk[-self.chunk_overlap:] if self.chunk_overlap else ""
                            current_chunk = overlap_text + sentence
                        else:
                            current_chunk = sentence
                    else:
                        current_chunk += sentence

        if current_chunk.strip():
            chunks.append(current_chunk.strip())

        return chunks

    def _split_prose(self, text: str) -> list[str]:
        """Split prose at paragraph or sentence boundaries."""
        # Prefer splitting at double newlines (paragraph breaks)
        paragraphs = re.split(r"\n\n+", text)
        result = []
        for para in paragraphs:
            if len(para) <= self.chunk_size:
                result.append(para + "\n\n")
            else:
                # Fall back to sentence splitting
                sentences = re.split(r"(?<=[.!?])\s+", para)
                for s in sentences:
                    result.append(s + " ")
        return result


# ══════════════════════════════════════════════════════════
# 4. DOCUMENT INGESTION PIPELINE
# ══════════════════════════════════════════════════════════

# The canonical Karpathy corpus — add/extend as needed
KARPATHY_CORPUS: list[dict] = [
    {
        "source_title": "The Unreasonable Effectiveness of Recurrent Neural Networks",
        "source_type": "blog",
        "date": "2015-05",
        "url": "http://karpathy.github.io/2015/05/21/rnn-effectiveness/",
        "career_phase": "stanford",
        "file_hint": "rnn_effectiveness.md",
    },
    {
        "source_title": "CS231n: Convolutional Neural Networks for Visual Recognition",
        "source_type": "lecture",
        "date": "2017",
        "url": "http://cs231n.stanford.edu/",
        "career_phase": "stanford",
        "file_hint": "cs231n_notes.md",
    },
    {
        "source_title": "Software 2.0",
        "source_type": "blog",
        "date": "2017-11",
        "url": "https://karpathy.medium.com/software-2-0-a64152b37c35",
        "career_phase": "tesla",
        "file_hint": "software_2_0.md",
    },
    {
        "source_title": "Tesla AI Day 2021",
        "source_type": "talk",
        "date": "2021-08",
        "url": "https://www.youtube.com/watch?v=j0z4FweCy4M",
        "career_phase": "tesla",
        "file_hint": "tesla_ai_day_2021.md",
    },
    {
        "source_title": "A Recipe for Training Neural Networks",
        "source_type": "blog",
        "date": "2019-04",
        "url": "http://karpathy.github.io/2019/04/25/recipe/",
        "career_phase": "tesla",
        "file_hint": "recipe_nn.md",
    },
    {
        "source_title": "Let's build GPT from scratch",
        "source_type": "youtube",
        "date": "2023-01",
        "url": "https://www.youtube.com/watch?v=kCc8FmEb1nY",
        "career_phase": "openai_v2",
        "file_hint": "build_gpt_scratch.md",
    },
    {
        "source_title": "Neural Networks: Zero to Hero — Micrograd",
        "source_type": "youtube",
        "date": "2022-09",
        "url": "https://www.youtube.com/watch?v=VMj-3S1tku0",
        "career_phase": "openai_v2",
        "file_hint": "micrograd.md",
    },
    {
        "source_title": "Neural Networks: Zero to Hero — Makemore",
        "source_type": "youtube",
        "date": "2022-10",
        "url": "https://www.youtube.com/watch?v=PaCmpygFfXo",
        "career_phase": "openai_v2",
        "file_hint": "makemore.md",
    },
    {
        "source_title": "Intro to Large Language Models",
        "source_type": "youtube",
        "date": "2023-11",
        "url": "https://www.youtube.com/watch?v=zjkBMFhNj_g",
        "career_phase": "openai_v2",
        "file_hint": "intro_llm.md",
    },
    {
        "source_title": "State of GPT (Microsoft Build 2023)",
        "source_type": "talk",
        "date": "2023-05",
        "url": "https://www.youtube.com/watch?v=bZQun8Y4L2A",
        "career_phase": "openai_v2",
        "file_hint": "state_of_gpt.md",
    },
    {
        "source_title": "Let's build the GPT Tokenizer",
        "source_type": "youtube",
        "date": "2024-02",
        "url": "https://www.youtube.com/watch?v=zduSFxRajkE",
        "career_phase": "openai_v2",
        "file_hint": "gpt_tokenizer.md",
    },
    {
        "source_title": "Eureka Labs — LLM101n announcement",
        "source_type": "blog",
        "date": "2024-07",
        "url": "https://github.com/karpathy/LLM101n",
        "career_phase": "eureka",
        "file_hint": "llm101n.md",
    },
    {
        "source_title": "rnn-effectiveness",
        "source_type": "blog",
        "date": "2015-05",
        "url": "http://karpathy.github.io/2015/05/21/rnn-effectiveness/",
        "career_phase": "stanford",
        "file_hint": "rnn-effectiveness.md",
    },
    {
        "source_title": "A Recipe for Training Neural Networks",
        "source_type": "blog",
        "date": "2019-04",
        "url": "http://karpathy.github.io/2019/04/25/recipe/",
        "career_phase": "openai_v1",
        "file_hint": "A Recipe for Training Neural Networks.md",
    },
    {
        "source_title": "Introduction",
        "source_type": "blog",
        "date": "2024-04",
        "url": "https://karpathy.ai/",
        "career_phase": "stanford",
        "file_hint": "Introduction.md",
    },
    {
        "source_title": "Software2",
        "source_type": "blog",
        "date": "2017-11",
        "url": "https://karpathy.medium.com/software-2-0-a64152b37c35",
        "career_phase": "openai_v1",
        "file_hint": "Software2.md",
    },
    {
        "source_title": "alphago-in-context",
        "source_type": "blog",
        "date": "2017-06",
        "url": "https://karpathy.medium.com/alphago-in-context-c47718cb95a5",
        "career_phase": "openai_v1",
        "file_hint": "alphago-in-context.md",
    },
    {
        "source_title": "icml-accepted-papers-institution-stats",
        "source_type": "blog",
        "date": "2017-04",
        "url": "https://karpathy.medium.com/icml-accepted-papers-institution-stats-bad8d2943f5d",
        "career_phase": "stanford",
        "file_hint": "icml-accepted-papers-institution-stats.md",
    },
    {
        "source_title": "a-peek-at-trends-in-machine-learning",
        "source_type": "blog",
        "date": "2017-04",
        "url": "https://karpathy.medium.com/a-peek-at-trends-in-machine-learning-ab8a1085a106",
        "career_phase": "stanford",
        "file_hint": "a-peek-at-trends-in-machine-learning.md",
    },
    {
        "source_title": "virtual-reality-still-not-quite-there-again",
        "source_type": "blog",
        "date": "2017-04",
        "url": "https://karpathy.medium.com/virtual-reality-still-not-quite-there-again-5f51f2b43867",
        "career_phase": "openai_v1",
        "file_hint": "virtual-reality-still-not-quite-there-again.md",
    },
    {
        "source_title": "virtual-reality-still-not-quite-there-again",
        "source_type": "blog",
        "date": "2017-01",
        "url": "https://karpathy.medium.com/virtual-reality-still-not-quite-there-again-5f51f2b43867",
        "career_phase": "openai_v1",
        "file_hint": "virtual-reality-still-not-quite-there-again.md",
    },
    {
        "source_title": "yes-you-should-understand-backprop",
        "source_type": "blog",
        "date": "2017-01",
        "url": "https://karpathy.medium.com/yes-you-should-understand-backprop-e2f06eab496b",
        "career_phase": "stanford",
        "file_hint": "yes-you-should-understand-backprop.md",
    },
    {
        "source_title": "microgpt",
        "source_type": "blog",
        "date": "2026-02",
        "url": "https://karpathy.github.io/2026/02/12/microgpt/",
        "career_phase": "openai_v2",
        "file_hint": "microgpt.md",
    },
    {
        "source_title": "Deep Neural Nets",
        "source_type": "blog",
        "date": "2022-03",
        "url": "https://karpathy.github.io/2022/03/14/lecun1989/",
        "career_phase": "openai_v2",
        "file_hint": "Deep Neural Nets.md",
    },
    {
        "source_title": "blockchain",
        "source_type": "blog",
        "date": "2021-06",
        "url": "https://karpathy.github.io/2021/06/21/blockchain/",
        "career_phase": "openai_v1",
        "file_hint": "blockchain.md",
    },
    {
        "source_title": "forward-pass",
        "source_type": "blog",
        "date": "2021-03",
        "url": "https://karpathy.github.io/2021/03/27/forward-pass/",
        "career_phase": "openai_v2",
        "file_hint": "forward-pass.md",
    },
    {
        "source_title": "biohacking-lite",
        "source_type": "blog",
        "date": "2020-06",
        "url": "https://karpathy.github.io/2020/06/11/biohacking-lite/",
        "career_phase": "openai_v1",
        "file_hint": "biohacking-lite.md",
    },
    {
        "source_title": "phd",
        "source_type": "blog",
        "date": "2016-09",
        "url": "https://karpathy.github.io/2016/09/07/phd/",
        "career_phase": "stanford",
        "file_hint": "phd.md",
    },
    {
        "source_title": "youtube_zjkBMFhNj_g",
        "source_type": "youtube",
        "date": "2023-11",
        "url": "https://www.youtube.com/watch?v=zjkBMFhNj_g",
        "career_phase": "openai_v1",
        "file_hint": "youtube_zjkBMFhNj_g.md",
    },
    {
        "source_title": "youtube_EWvNQjAaOHw",
        "source_type": "youtube",
        "date": "2025-02",
        "url": "https://www.youtube.com/watch?v=EWvNQjAaOHw",
        "career_phase": "openai_v1",
        "file_hint": "youtube_EWvNQjAaOHw.md",
    },
    {
        "source_title": "youtube_kCc8FmEb1nY",
        "source_type": "youtube",
        "date": "2023-01",
        "url": "https://www.youtube.com/watch?v=kCc8FmEb1nY",
        "career_phase": "openai_v1",
        "file_hint": "youtube_kCc8FmEb1nY.md",
    },
    {
        "source_title": "youtube_zduSFxRajkE",
        "source_type": "youtube",
        "date": "2024-02",
        "url": "https://www.youtube.com/watch?v=zduSFxRajkE",
        "career_phase": "openai_v2",
        "file_hint": "youtube_zduSFxRajkE.md",
    },
    {
        "source_title": "youtube_VMj-3S1tku0",
        "source_type": "youtube",
        "date": "2022-08",
        "url": "https://www.youtube.com/watch?v=VMj-3S1tku0",
        "career_phase": "openai_v1",
        "file_hint": "youtube_VMj-3S1tku0.md",
    },
    {
        "source_title": "youtube_PaCmpygFfXo",
        "source_type": "youtube",
        "date": "2022-09",
        "url": "https://www.youtube.com/watch?v=PaCmpygFfXo",
        "career_phase": "openai_v2",
        "file_hint": "youtube_PaCmpygFfXo.md",
    },
    {
        "source_title": "youtybe_48-state-of-gpt",
        "source_type": "youtube",
        "date": "2023-05",
        "url": "https://www.youtube.com/watch?v=bZQun8Y4L2A",
        "career_phase": "openai_v2",
        "file_hint": "youtybe_48-state-of-gpt-brk216hfs-youtube-20260605-1716.md",
    },
    {
        "source_title": "youtybe_j0z4FweCy4M",
        "source_type": "youtube",
        "date": "2021-08",
        "url": "https://www.youtube.com/watch?v=j0z4FweCy4M",
        "career_phase": "tesla",
        "file_hint": "youtube_j0z4FweCy4M.md",
    },
    {
        "source_title": "youtybe_NfnWJUyUJYU",
        "source_type": "youtube",
        "date": "2016-01",
        "url": "https://www.youtube.com/watch?v=NfnWJUyUJYU",
        "career_phase": "stanford",
        "file_hint": "youtube_NfnWJUyUJYU.md",
    },
    {
        "source_title": "youtybe_8inugqHkfvE",
        "source_type": "youtube",
        "date": "2016-01",
        "url": "https://www.youtube.com/watch?v=8inugqHkfvE",
        "career_phase": "openai_v1",
        "file_hint": "youtube_8inugqHkfvE.md",
    },
    {
        "source_title": "youtybe_qlLChbHhbg4",
        "source_type": "youtube",
        "date": "2016-01",
        "url": "https://www.youtube.com/watch?v=qlLChbHhbg4",
        "career_phase": "openai_v1",
        "file_hint": "youtube_qlLChbHhbg4.md",
    },
    {
        "source_title": "youtybe_i94OvYb6noo",
        "source_type": "youtube",
        "date": "2016-01",
        "url": "https://www.youtube.com/watch?v=i94OvYb6noo",
        "career_phase": "openai_v1",
        "file_hint": "youtube_i94OvYb6noo.md",
    },
    {
        "source_title": "youtybe_gYpoJMlgyXA",
        "source_type": "youtube",
        "date": "2016-01",
        "url": "https://www.youtube.com/watch?v=gYpoJMlgyXA",
        "career_phase": "openai_v1",
        "file_hint": "youtube_gYpoJMlgyXA.md",
    },
    {
        "source_title": "youtybe_hd_KFJ5ktUc",
        "source_type": "youtube",
        "date": "2016-01",
        "url": "https://www.youtube.com/watch?v=hd_KFJ5ktUc",
        "career_phase": "openai_v1",
        "file_hint": "youtube_hd_KFJ5ktUc.md",
    },
    {
        "source_title": "youtybe_GxZrEKZfW2o",
        "source_type": "youtube",
        "date": "2016-01",
        "url": "https://www.youtube.com/watch?v=GxZrEKZfW2o",
        "career_phase": "openai_v1",
        "file_hint": "youtube_GxZrEKZfW2o.md",
    },
    {
        "source_title": "youtybe_ta5fdaqDT3M",
        "source_type": "youtube",
        "date": "2016-01",
        "url": "https://www.youtube.com/watch?v=ta5fdaqDT3M",
        "career_phase": "openai_v1",
        "file_hint": "youtube_ta5fdaqDT3M.md",
    },
    {
        "source_title": "youtybe_96jN2OCOfLs",
        "source_type": "youtube",
        "date": "2026-04",
        "url": "https://www.youtube.com/watch?v=96jN2OCOfLs",
        "career_phase": "openai_v1",
        "file_hint": "youtube_96jN2OCOfLs.md",
    },
]


class KarpathyRAGPipeline:
    """
    Full RAG pipeline:
      - ChromaDB vector store with Google Generative AI embeddings
      - Code-aware chunking via KarpathyMarkdownSplitter
      - Timeline metadata on every chunk
      - Filtered retrieval (semantic + career_phase filter)
    """

    COLLECTION_NAME = "karpathy_twin_v1"

    def __init__(
        self,
        persist_dir: str = "./data/chromadb",
        google_api_key: str = "",
        embedding_model: str = "models/gemini-embedding-001",
    ):
        self.persist_dir = persist_dir
        self.splitter = KarpathyMarkdownSplitter()

        # ChromaDB client (persistent)
        self.client = chromadb.PersistentClient(path=persist_dir)

        # Embedding function — Google Generative AI
        self.embedding_fn = SafeGeminiEmbeddings(
            api_key=google_api_key,
            model_name=embedding_model,
        )

        self.collection = self.client.get_or_create_collection(
            name=self.COLLECTION_NAME,
            embedding_function=self.embedding_fn,
            metadata={"hnsw:space": "cosine"},
        )

    # ── Ingestion ──────────────────────────────────────────

    def ingest_text(self, text: str, meta: SourceMetadata) -> int:
        """Chunk text and upsert into ChromaDB. Returns number of chunks added."""
        chunks = self.splitter.split_text(text)
        if not chunks:
            return 0

        documents, metadatas, ids = [], [], []
        for i, chunk in enumerate(chunks):
            chunk_meta = SourceMetadata(
                source_title=meta.source_title,
                source_type=meta.source_type,
                date=meta.date,
                career_phase=meta.career_phase,
                url=meta.url,
                chunk_index=i,
                has_code=bool(re.search(r"```", chunk)),
                language=meta.language,
            )
            # Stable ID: hash of (source + chunk content)
            chunk_id = hashlib.sha256(
                f"{meta.source_title}::{i}::{chunk[:80]}".encode()
            ).hexdigest()[:24]

            documents.append(chunk)
            metadatas.append(chunk_meta.to_chroma_meta())
            ids.append(chunk_id)

        # Batch upsert
        self.collection.upsert(documents=documents, metadatas=metadatas, ids=ids)
        return len(chunks)

    def ingest_file(self, filepath: str, corpus_entry: dict) -> int:
        """Read a local markdown/txt file and ingest it."""
        p = Path(filepath)
        if not p.exists():
            print(f"[RAG] File not found: {filepath} — skipping.")
            return 0
        text = p.read_text(encoding="utf-8")
        meta = SourceMetadata(
            source_title=corpus_entry["source_title"],
            source_type=corpus_entry["source_type"],
            date=corpus_entry["date"],
            career_phase=corpus_entry.get("career_phase", detect_career_phase(text)),
            url=corpus_entry.get("url", ""),
        )
        n = self.ingest_text(text, meta)
        print(f"[RAG] Ingested '{corpus_entry['source_title']}': {n} chunks")
        return n

    # ── Retrieval ──────────────────────────────────────────

    def retrieve(
        self,
        query: str,
        n_results: int = 5,
        career_phase_filter: Optional[str] = None,
    ) -> list[dict]:
        """
        Retrieve top-N chunks for a query.
        Optionally filter by career_phase for timeline-aware retrieval.
        Returns list of {text, metadata, distance} dicts.
        """
        where = None
        if career_phase_filter and career_phase_filter != "general":
            where = {"career_phase": {"$eq": career_phase_filter}}

        try:
            results = self.collection.query(
                query_texts=[query],
                n_results=min(n_results, self.collection.count() or 1),
                where=where,
                include=["documents", "metadatas", "distances"],
            )
        except Exception:
            # Fallback: no filter if collection is small
            results = self.collection.query(
                query_texts=[query],
                n_results=min(n_results, max(1, self.collection.count())),
                include=["documents", "metadatas", "distances"],
            )

        chunks = []
        if results and results["documents"]:
            for doc, meta, dist in zip(
                results["documents"][0],
                results["metadatas"][0],
                results["distances"][0],
            ):
                chunks.append({"text": doc, "metadata": meta, "distance": dist})

        return chunks

    def retrieve_with_context(
        self,
        query: str,
        n_results: int = 5,
        career_phase_filter: Optional[str] = None,
    ) -> tuple[str, str]:
        """
        Higher-level retrieval: returns (formatted_context_string, timeline_description).
        Ready to be injected into the system prompt.
        """
        chunks = self.retrieve(query, n_results, career_phase_filter)
        if not chunks:
            return "", ""

        # Detect timeline from the query itself
        query_phase = detect_career_phase(query)
        timeline_desc = get_timeline_description(query_phase)

        # Format context block
        context_parts = []
        for i, chunk in enumerate(chunks, 1):
            m = chunk["metadata"]
            citation = f'[Source: "{m["source_title"]}", {m["source_type"]}, {m["date"]}]'
            relevance = f"(relevance: {1 - chunk['distance']:.2f})"
            code_flag = " [contains code]" if m.get("has_code") else ""
            header = f"--- RETRIEVED CHUNK {i} {citation}{code_flag} {relevance} ---"
            context_parts.append(f"{header}\n{chunk['text']}")

        return "\n\n".join(context_parts), timeline_desc

    def collection_stats(self) -> dict:
        count = self.collection.count()
        return {"total_chunks": count, "collection": self.COLLECTION_NAME}


# ══════════════════════════════════════════════════════════
# 5. DEMO INGESTION SCRIPT
# ══════════════════════════════════════════════════════════

DEMO_CONTENT = {
    "software_2_0.md": """
# Software 2.0

I sometimes see people refer to neural networks as "just another tool in your machine learning toolbox". 
They have some pros and cons, they work here or there, and sometimes you can use them to win Kaggle competitions.

I am becoming increasingly convinced that this is not the right way to think about them. 
Here's a better framing: **Software 2.0 is written in neural network weights.**

## The Core Idea

In Software 1.0, a human programmer writes explicit instructions:

```python
def is_spam(email):
    keywords = ["win", "prize", "click here"]
    return any(kw in email.lower() for kw in keywords)
```

In Software 2.0, we define the desired behavior through a dataset, and the optimization (gradient descent) 
writes the program for us into the weights:

```python
# Software 2.0: define the dataset and loss, let SGD find the weights
model = Transformer(vocab_size=50257, n_layer=12, n_head=12, n_embd=768)
optimizer = torch.optim.AdamW(model.parameters(), lr=3e-4)

for batch in dataloader:
    logits, loss = model(batch['input_ids'], batch['labels'])
    optimizer.zero_grad()
    loss.backward()  # the backward pass: gradient flows back through the compute graph
    optimizer.step()
```

The benefits of Software 2.0: it's often more accurate, it can be parallelized on GPUs, 
and it can generalize in ways that hand-coded rules never could. The downside: 
**it's harder to interpret, it fails in unpredictable ways, and the network is a leaky abstraction 
over the data distribution you trained on**.

## Where it's already happening

- **Vision**: CNNs replaced hand-crafted feature descriptors (SIFT, HOG, etc.)
- **Speech**: End-to-end models replaced HMMs + hand-tuned features  
- **Translation**: Neural MT replaced rule-based + phrase-based systems
- **Game playing**: AlphaGo replaced Monte Carlo Tree Search heuristics

The 2.0 stack has occupied and is winning in most problem domains.
""",
"build_gpt_scratch.md": '''
# Let's Build GPT From Scratch

The goal of this tutorial is to build a GPT-like model from scratch.
We're going to start with a simple bigram language model and work up to the full transformer.

## The Setup

First, let me define what we're doing. We have a text corpus (I'll use Shakespeare).
We want to train a model that can generate text character by character, or token by token.

**This is the essence of what GPT is doing — it's a sequence model predicting the next token.**

## Step 1: Tokenization

For simplicity, let's use character-level tokenization:

```python
# read the corpus
with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# all unique characters
chars = sorted(list(set(text)))
vocab_size = len(chars)
print(''.join(chars))  # !$&', -.3:;?ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
print(vocab_size)  # 65

# tokenizer: simple char-to-int mapping
stoi = { ch:i for i,ch in enumerate(chars) }
itos = { i:ch for i,ch in enumerate(chars) }
encode = lambda s: [stoi[c] for c in s]
decode = lambda l: ''.join([itos[i] for i in l])

## Step 2: Self-Attention — The Heart of the Transformer

The key insight is **communication between tokens**. Every token needs to look at the other tokens
and decide what information to aggregate.

```python
class Head(nn.Module):
    """One head of self-attention — the fundamental building block."""
    
    def __init__(self, head_size):
        super().__init__()
        self.key   = nn.Linear(n_embd, head_size, bias=False)
        self.query = nn.Linear(n_embd, head_size, bias=False)
        self.value = nn.Linear(n_embd, head_size, bias=False)
        self.register_buffer('tril', torch.tril(torch.ones(block_size, block_size)))
        self.dropout = nn.Dropout(dropout)

    def forward(self, x):
        B, T, C = x.shape
        k = self.key(x)    # (B, T, head_size)
        q = self.query(x)  # (B, T, head_size)
        
        # Scaled dot-product attention
        # "affinities" — how much does each token attend to each other token?
        wei = q @ k.transpose(-2, -1) * (k.shape[-1] ** -0.5)  # (B, T, T)
        wei = wei.masked_fill(self.tril[:T, :T] == 0, float('-inf'))  # causal mask
        wei = F.softmax(wei, dim=-1)  # normalize: weights sum to 1
        wei = self.dropout(wei)
        
        # Weighted aggregation of values
        v = self.value(x)  # (B, T, head_size)
        out = wei @ v       # (B, T, head_size)
        return out
```

Notice: the `tril` mask is what makes this a **decoder** (causal) model.
Tokens can only look *back* in time, never forward. At inference time, this doesn't matter —
we generate left to right anyway.

## Why Attention Works

Think about it from first principles. Each token emits:
- A **query**: "what am I looking for?"
- A **key**: "what do I have to offer?"  
- A **value**: "what information will I actually pass if attended to?"

The dot product of Q and K gives you the affinity. Softmax normalizes it.
Then we do a weighted sum of V. **It's a differentiable, learnable lookup table.**

The network is just learning to route information between tokens in a task-relevant way.
It's not magic, it's just matrix multiplications with a masking trick.
''',
    "recipe_nn.md": """
# A Recipe for Training Neural Networks

The first thing I want you to understand is that training a neural network is not a matter of magic. 
It is a matter of engineering discipline.

## The Most Common Mistake

Most people who are new to neural networks think debugging looks like debugging code. 
It doesn't. **The network will always run. It will always produce a number for the loss. 
It will silently fail in ways that take days or weeks to discover.**

I've seen this pattern hundreds of times at Tesla. Someone trains a model, the loss goes down, 
they ship it, and then it fails on a weird edge case they never thought to check for.

## My Recommended Process

### Step 0: Become One With the Data

Spend time looking at your raw data. Don't skip this step.
I mean actually look at thousands of examples. 

```python
# Don't use matplotlib and call it a day.
# Write a custom visualizer. Understand what you're feeding the model.
for i in range(100):
    sample = dataset[i]
    print(f"Sample {i}: shape={sample['image'].shape}, label={sample['label']}")
    # Look for: corrupted files, mislabeled examples, class imbalance, 
    # distribution shifts, weird outliers
```

### Step 1: Set Up the End-to-End Training Skeleton First

Train a tiny model on a tiny dataset. Make sure everything works before scaling.

```python
# The single most valuable debugging trick I know:
# Overfit a single batch.
# If you can't overfit 1 batch, your model or training loop is broken.
x, y = next(iter(train_loader))  # grab ONE batch
for i in range(200):
    logits = model(x)
    loss = criterion(logits, y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    if i % 20 == 0:
        print(f"step {i}: loss = {loss.item():.4f}")
# Loss should go to ~0. If it doesn't, debug.
```

### Step 2: Overfit, Then Regularize

Your goal sequence should always be:
1. Get a model that *can* overfit your training data (high capacity)
2. Then add regularization (dropout, weight decay, data augmentation) to improve validation

Never try to regularize a model that isn't overfitting first.
That's like trying to slow down a car that isn't moving.

### Step 3: Tune Hyperparameters Systematically

The learning rate is the most important hyperparameter.

```python
# Learning rate finder: a classic technique
lrs = torch.logspace(-5, -1, 100)  # try 100 log-spaced LR values
losses = []
for lr in lrs:
    optimizer = torch.optim.SGD(model.parameters(), lr=lr.item())
    loss = train_one_step(model, optimizer, batch)
    losses.append(loss)

# Plot losses vs lr — pick the lr just before the loss explodes
import matplotlib.pyplot as plt
plt.plot(lrs, losses)
plt.xscale('log')
plt.xlabel('learning rate')
plt.ylabel('loss')
plt.show()
```

The vibes of good training: loss should decrease smoothly, 
gradient norms should be stable, activations shouldn't be saturating.
""",
}


def bootstrap_demo_data(pipeline: KarpathyRAGPipeline, data_dir: str = "./data/corpus") -> int:
    """
    Ingest the hardcoded demo content. In production, replace with real scraped files.
    """
    Path(data_dir).mkdir(parents=True, exist_ok=True)
    total = 0
    for filename, content in DEMO_CONTENT.items():
        # Find matching corpus entry
        corpus_entry = next(
            (e for e in KARPATHY_CORPUS if e.get("file_hint") == filename),
            None
        )
        if corpus_entry is None:
            continue
        # Write file locally (for reference)
        fpath = Path(data_dir) / filename
        fpath.write_text(content, encoding="utf-8")
        # Ingest
        meta = SourceMetadata(
            source_title=corpus_entry["source_title"],
            source_type=corpus_entry["source_type"],
            date=corpus_entry["date"],
            career_phase=corpus_entry["career_phase"],
            url=corpus_entry.get("url", ""),
        )
        n = pipeline.ingest_text(content, meta)
        total += n
        print(f"  ✓ '{corpus_entry['source_title']}' → {n} chunks")
    return total
