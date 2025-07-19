from textstat import flesch_reading_ease, flesch_kincaid_grade

def compute_reward(text):
    readability = flesch_reading_ease(text)
    grade_level = flesch_kincaid_grade(text)
    reward = max(0.1, min(1.0, (readability / 100)))  # Scale between 0.1 and 1.0
    return {"readability": readability, "grade_level": grade_level, "reward": reward}