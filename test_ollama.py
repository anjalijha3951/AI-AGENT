import ollama

response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content": "Explain an AI agent in simple words."
        }
    ]
)

print(response["message"]["content"])