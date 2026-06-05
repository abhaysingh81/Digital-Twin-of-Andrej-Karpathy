## 📁 Project Structure

```
karpathy-twin/
│
├── app.py                          # Streamlit UI (Section 5)
│
├── core/
│   ├── __init__.py
│   ├── agent.py                    # Main orchestrator (Section 2–4 glue)
│   └── system_prompt.py           # Karpathy persona prompt (Section 4)
│
├── rag/
│   ├── __init__.py
│   └── pipeline.py                # RAG engine: splitter, ChromaDB, retrieval
│
├── memory/
│   ├── __init__.py
│   └── memory_manager.py          # Dual-layer memory (Section 3)
│
├── sample_conversations/
│   └── eval_prompts.py            # 20 evaluation prompts + 10 sample convos
│
├── data/                          # Auto-created on first run
│   ├── chromadb/                  # Persistent vector store
│   ├── corpus/                    # Markdown source files
│   └── memory/
│       └── user_profile.json      # Long-term user profile
│
├── requirements.txt
└── README.md
```

---