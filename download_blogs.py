from pathlib import Path
import requests
from bs4 import BeautifulSoup
import html2text

def download_webpage_as_md(url: str, output_filename: str):
    # Create the directory if it doesn't exist
    output_dir = Path("data/corpus")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Avoid getting blocked by using a standard browser user-agent header
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    try:
        # 1. Fetch the webpage content
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        # 2. Parse the HTML and extract the core text body
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Optional: Clean up junk elements like scripts, styles, and navbars
        for element in soup(["script", "style", "nav", "footer", "header"]):
            element.decompose()
            
        # 3. Convert HTML directly to clean Markdown
        converter = html2text.HTML2Text()
        converter.ignore_links = False  # Keep links intact for metadata URLs
        converter.bypass_tables = False # Keep tables well-formatted
        markdown_text = converter.handle(str(soup))
        
        # 4. Save to the corpus path
        filepath = output_dir / output_filename
        filepath.write_text(markdown_text, encoding="utf-8")
        print(f"✓ Successfully saved: {url} -> {filepath}")
        
    except Exception as e:
        print(f"✗ Failed to download {url}: {e}")

# --- Example Usage ---
if __name__ == "__main__":
    # Example: Ingesting Karpathy's famous "Software 2.0" blog
    blog_url = "https://karpathy.github.io/2016/09/07/phd/"
    download_webpage_as_md(blog_url, "phd.md")