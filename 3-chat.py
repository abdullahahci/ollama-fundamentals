import ollama

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role":"user", "content":"Why the sky is red"
        }
    ]
)

print(response["message"]["content"])

