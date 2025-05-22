import ollama

# Initialize with an empty history
chat_history = []

while True:
    user_input = input("\nYou: \n")
    chat_history.append({"role": "system", "content": "Your name is Mario, you are a joyful person, give short and precise answers."})
    chat_history.append({"role": "user", "content": user_input})
    
    # Generate assistant response
    response = ollama.chat(
        model="llama3.2",
        messages=chat_history,
        options={
            "temperature":1,  # Optional: control randomness (higher = more creative)
            "top_k":50,         # Optional: limit the number of candidate tokens
            "top_p":1.0,         # Optional: nucleus sampling parameter
        },
        stream=True,
  
    )
    
    # Stream the response
    assistant_response = ""
    print("Assistant:")
    for chunk in response:
        message_chunk = chunk['message']['content']
        print(message_chunk, end="", flush=True)
        assistant_response += message_chunk
    

    chat_history.append({"role": "assistant", "content": assistant_response})
