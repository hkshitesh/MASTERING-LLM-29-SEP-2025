import requests
import base64

with open("digit.png", "rb") as f:
    img_base64 = base64.b64encode(f.read()).decode("utf-8")

response = requests.post("http://localhost:8000/predict/", json={"image_base64": img_base64})
print(response.json())
