import ollama

res = ollama.generate(
    model="llama3.2",
    prompt="Tell me a funny story",
    stream=True
)

for chunk in res:
    print(chunk["response"], end="", flush=True)