# ui/main_ui.py

import sys
import asyncio

# ✅ Fix for Windows Playwright subprocess issue
if sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from scraping.fetch_and_screenshot import fetch_chapter_and_screenshot
from ai_writer.spin_content import spin_text
from rl.reward_logic import compute_reward
from database.chromadb_interface import save_version

st.set_page_config(page_title="📚 Automated Book Publisher", layout="centered")

st.title("📚 Automated Book Publication System")
st.markdown("This app scrapes a chapter, rewrites it using AI, scores it, and stores the version.")

# URL input
url = st.text_input("📥 Enter Chapter URL:", "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1")

# Button to run the full pipeline
if st.button("🚀 Run Full Pipeline"):
    st.info("📡 Fetching content and screenshot...")
    fetch_chapter_and_screenshot(url, "data/raw")

    # Read raw text
    with open("data/raw/raw_text.txt", "r", encoding="utf-8") as f:
        raw = f.read()

    st.success("✅ Chapter fetched successfully!")

    # Spin text using AI
    st.info("🤖 Rewriting content with AI...")
    spun = spin_text(raw)
    st.success("✅ Content rewritten!")

    # Evaluate reward
    st.info("📊 Scoring rewritten content...")
    scores = compute_reward(spun)

    # Save spun version in vector DB
    save_version(spun, "v1", {"url": url, **scores})

    # Display results
    st.success("🎉 Done! Process completed and version saved.")
    st.subheader("📝 Rewritten Chapter")
    st.text(spun)
