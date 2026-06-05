import re
from pathlib import Path

def auto_register_source(filepath: str, source_title: str, source_type: str, url: str = "", date: str = "2026-01"):
    """
    Analyzes a file, generates the corpus dictionary entry, and appends it 
    directly into the KARPATHY_CORPUS list inside rag/pipeline.py.
    """
    file_path = Path(filepath)
    if not file_path.exists():
        print(f"❌ Error: The file {filepath} does not exist.")
        return

    # Read content to scan for career phase keywords
    text_content = file_path.read_text(encoding="utf-8").lower()
    
    # Simple heuristic to guess the career phase based on keywords
    phase_keywords = {
        "stanford": ["cs231n", "convnet", "lstm", "fei-fei li", "stanford"],
        "openai_v1": ["reinforcement learning", "ppo", "gan", "dota"],
        "tesla": ["autopilot", "fsd", "vision", "hydranet", "occupancy", "tesla"],
        "openai_v2": ["gpt", "transformer", "attention", "bpe", "nanogpt", "makemore", "zero to hero"],
        "eureka": ["eureka labs", "llm101n", "ai tutor", "education"]
    }
    
    detected_phase = "general"
    max_matches = 0
    for phase, keywords in phase_keywords.items():
        matches = sum(1 for kw in keywords if kw in text_content)
        if matches > max_matches:
            max_matches = matches
            detected_phase = phase

    # Generate the dictionary string formatting
    entry_string = f"""    {{
        "source_title": "{source_title}",
        "source_type": "{source_type}",
        "date": "{date}",
        "url": "{url}",
        "career_phase": "{detected_phase}",
        "file_hint": "{file_path.name}",
    }},
"""

    # Target file
    pipeline_path = Path(r"D:\AIMS\karpathy-twin\karpathy-twin\rag\pipeline.py")
    if not pipeline_path.exists():
        print("❌ Error: rag/pipeline.py not found. Make sure you run this from the root directory.")
        return

    pipeline_content = pipeline_path.read_text(encoding="utf-8")

    # Locate the closing bracket of KARPATHY_CORPUS = [ ... ]
    # We find where KARPATHY_CORPUS starts and grab the closing bracket matching it
    corpus_match = re.search(r"KARPATHY_CORPUS:\s*list\[dict\]\s*=\s*\[", pipeline_content)
    if not corpus_match:
        print("❌ Error: Could not locate 'KARPATHY_CORPUS: list[dict] = [' inside pipeline.py.")
        return

    # Find the closing square bracket of the list
    start_idx = corpus_match.end()
    bracket_count = 1
    insert_idx = -1
    
    for i in range(start_idx, len(pipeline_content)):
        if pipeline_content[i] == '[':
            bracket_count += 1
        elif pipeline_content[i] == ']':
            bracket_count -= 1
            if bracket_count == 0:
                insert_idx = i
                break

    if insert_idx == -1:
        print("❌ Error: Could not find the end of the KARPATHY_CORPUS list.")
        return

    # Inject the new entry right before the closing bracket ']'
    updated_content = pipeline_content[:insert_idx] + entry_string + pipeline_content[insert_idx:]
    pipeline_path.write_text(updated_content, encoding="utf-8")
    
    print(f"✅ Successfully registered '{source_title}' to rag/pipeline.py under phase '{detected_phase}'!")

# --- Example Usage ---
if __name__ == "__main__":
    # Point this to a file you just downloaded/created in data/corpus/
    auto_register_source(
        filepath=r"D:\AIMS\karpathy-twin\karpathy-twin\data\corpus\youtube_96jN2OCOfLs.md",
        source_title="youtybe_96jN2OCOfLs",
        source_type="youtube",
        url="https://www.youtube.com/watch?v=96jN2OCOfLs",
        date="2026-04"
    )