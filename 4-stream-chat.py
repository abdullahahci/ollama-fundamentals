import ollama

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role":"user", "content":"Why the sky is red"
        }
    ],
    stream=True
)

for res in response:
    print(res["message"]["content"], end="", flush=True)