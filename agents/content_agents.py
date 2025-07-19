import openai

# General function to call LLM agent with a role
def call_llm(role_prompt, content):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": role_prompt},
            {"role": "user", "content": content}
        ]
    )
    return response['choices'][0]['message']['content']

# Agent that spins raw content
def WriterAgent(raw_text):
    role_prompt = "You are an AI Writer. Rewrite the chapter to improve clarity and flow while preserving its original meaning."
    return call_llm(role_prompt, raw_text)

# Agent that reviews and suggests improvements
def ReviewerAgent(spun_text):
    role_prompt = "You are an AI Reviewer. Provide feedback on grammar, coherence, and style. Rewrite where necessary for improvement."
    return call_llm(role_prompt, spun_text)

# Agent that edits based on review
def EditorAgent(reviewed_text):
    role_prompt = "You are an AI Editor. Finalize the text based on reviewer suggestions. Ensure polish, clarity, and correctness."
    return call_llm(role_prompt, reviewed_text)
