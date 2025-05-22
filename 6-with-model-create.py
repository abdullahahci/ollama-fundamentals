
from ollama import generate, create, delete

params = {
    'temperature': 0.7,           # Controls randomness: lower = more deterministic, higher = more creative
    'top_p': 0.9,                 # Nucleus sampling: considers tokens with cumulative probability up to top_p
    'top_k': 50,                  # Considers only the top_k most probable tokens
    'repeat_penalty': 1.1,        # Penalizes repetition: values >1.0 discourage repeating the same phrases
    'presence_penalty': 0.6,      # Encourages introducing new topics: higher values promote diversity
    'frequency_penalty': 0.5,     # Penalizes frequent tokens: reduces overuse of common words
    'num_ctx': 4096,              # Context window size: number of tokens the model considers from the prompt
    'num_predict': 256,           # Maximum number of tokens to generate in the response
    'stop': ['\nUser:', '\nSystem:'],  # Sequences where the model will stop generating further text
    'seed': 42                    # Sets the random seed for reproducibility
    }
create(model='assistant', from_='llama3.2', system="You are a very smart assistant who knows everything about everything in daily life. You are very funny, direct and informative.", parameters={"temperature":0.5})


res = generate(model="assistant", prompt="Tell me a tip?")
print(res["response"])


# delete model
delete("assistant")