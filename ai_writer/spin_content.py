import openai

def spin_text(content):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI writer that paraphrases book chapters for clarity and richness."},
            {"role": "user", "content": content}
        ]
    )
    return response["choices"][0]["message"]["content"]
