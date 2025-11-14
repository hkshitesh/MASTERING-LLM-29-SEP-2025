import requests
response = requests.post("http://localhost:8000/generate/", json={"prompt": "The future of AI is"})
print(response.json())
