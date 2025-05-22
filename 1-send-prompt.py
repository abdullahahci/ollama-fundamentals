import requests
import json

url = 'http://localhost:11434/api/generate'
data = {
    "model": "llama3.2",
    "prompt":"Why is the sky blue?",
    "stream": False
}

response = requests.post(url, json=data, stream=True)

#check the response status
if response.status_code == 200:
    print("Generated text:", end="", flush=True)
    for line in response.iter_lines():
        if line:
            decoded_line = line.decode("utf-8")
            result = json.loads(decoded_line)
            generated_text = result.get("response", "")
            print(generated_text, end="", flush=True)


else:
    print("Error, response is ", response.status_code, response.text)