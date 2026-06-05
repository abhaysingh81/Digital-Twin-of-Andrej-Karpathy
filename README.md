# Karpathy Digital Twin

AIMS SUMMER PROJECT 1

The Karpathy Digital Twin is an interactive AI mentoring system designed to replicate the teaching philosophy, deep technical expertise, and signature Socratic style of AI researcher Andrej Karpathy.

Moving beyond a simple API wrapper, this project is built "from scratch" to solve the exact problems that cause standard AI assistants to fail at teaching computer science. Powered by Gemini 2.5 Flash, the architecture relies on three custom pillars:

Code-Aware RAG Pipeline: A custom retrieval engine that treats mathematical formulas and code blocks as atomic units, ensuring the model always references unbroken, fully executable scripts.

Timeline-Aware Context Router: A dynamic classifier that prevents historical mix-ups by rooting the AI's answers in the correct era of his career (e.g., Stanford, Tesla Autopilot, or Eureka Labs).

Dual-Layer Memory System: A cognitive architecture that uses a short-term buffer for fluid conversation and a background extraction agent to permanently remember your specific coding background, active projects, and learning goals.

## ✨ What It Does

1. Teaches like Karpathy: Instead of acting like a generic AI assistant, the prompt forces the model to teach from first principles, matching how Andrej actually talks. It uses his signature phrases ("leaky abstraction," "from scratch") and prioritizes writing raw PyTorch code over giving vague, high-level summaries.

2. Never breaks your code: Standard AI retrieval pipelines blindly chop up documents, which ruins Python scripts. We built a custom code-aware splitter that safely slices conversational text but keeps complex neural network code blocks 100% intact, ensuring the AI always references working, executable code.

3. Knows when you're asking about: Because Andrej's career spans everything from early Stanford CNNs to Tesla's Autopilot to Eureka Labs, the app dynamically detects the era of your question. It filters the database to that specific timeframe so you don't get 2024 LLM advice for a 2017 autonomous driving question.

4. Remembers your coding journey: While a short-term buffer handles the back-and-forth of your active chat, a quiet background agent extracts facts about your coding experience, active projects, and bug struggles. It saves this to a local profile so the next time you launch the app, the Twin already knows your background and tailors its advice instantly.

## 📁 Folder Structure

```text
karpathy-twin/
├── app.py                      # Main Streamlit UI, chat interface, and UI routing
├── .env                        # Environment variables (e.g., GOOGLE_API_KEY)
├── core/
│   ├── agent.py                # Main orchestrator tying Gemini, RAG, and Memory together
│   └── system_prompts.py       # Dynamic, context-injected persona instructions
├── rag/
│   └── pipeline.py             # ChromaDB vector store, custom code splitter, & timeline routing
├── memory/
│   └── memory_manager.py       # Short-term buffer & Long-term background fact extraction
└── data/                       # Local storage (created automatically)
    ├── chromadb/               # Persistent vector database 
    ├── corpus/                 # Markdown files containing Andrej's blogs, talks, and transcripts
    └── memory/                 # user_profile.json (Persistent user facts)