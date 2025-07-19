from agents.content_agents import WriterAgent, ReviewerAgent, EditorAgent

with open("data/raw/raw_text.txt", "r") as f:
    raw = f.read()

spun = WriterAgent(raw)
reviewed = ReviewerAgent(spun)
final = EditorAgent(reviewed)

with open("data/raw/spin_v1.txt", "w") as f:
    f.write(spun)
with open("data/raw/spin_v2.txt", "w") as f:
    f.write(reviewed)
with open("data/raw/final_v1.txt", "w") as f:
    f.write(final)

print("✅ Writer, Reviewer, and Editor steps completed.")
