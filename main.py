from scraping.fetch_and_screenshot import fetch_chapter_and_screenshot
from ai_writer.spin_content import spin_text
from rl.reward_logic import compute_reward
from database.chromadb_interface import save_version
from agents.voice_interface import speak

url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
save_path = "data/raw"

fetch_chapter_and_screenshot(url, save_path)

with open(f"{save_path}/raw_text.txt", "r", encoding="utf-8") as f:
    content = f.read()

spun = spin_text(content)
scores = compute_reward(spun)
save_version(spun, "v1", {"url": url, **scores})
speak("Processing complete. Content saved.")
