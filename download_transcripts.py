from youtube_transcript_api import YouTubeTranscriptApi
import os

# Ensure the directory exists
os.makedirs("data/corpus", exist_ok=True)

# Replace this with the video ID from the YouTube URL (the part after v=)
video_id = "96jN2OCOfLs" # Example: Hacker's Guide to Language Models

try:
    # 1. Instantiate the API client
    yt_api = YouTubeTranscriptApi()
    
    # 2. Fetch the transcript using the new method
    transcript = yt_api.fetch(video_id)
    
    # 3. Combine the text fragments (accessing the .text attribute)
    full_text = "\n".join([chunk.text for chunk in transcript])
    
    # Define the filename
    filename = f"youtube_{video_id}.md"
    filepath = f"data/corpus/{filename}"
    
    # Save it as a markdown file
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# YouTube Transcript: {video_id}\n\n{full_text}")
        
    print(f"Success! Saved to {filepath}")
    print(f"Your file_hint for pipeline.py is: {filename}")

except Exception as e:
    print(f"Error downloading transcript: {e}")