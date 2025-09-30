from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline, set_seed

app = FastAPI()

generator = pipeline("text-generation", model="distilgpt2")
set_seed(42)

class Prompt(BaseModel):
    prompt: str

@app.post("/generate/")
def generate_text(data: Prompt):
    result = generator(data.prompt, max_length=50, num_return_sequences=1)
    return {"generated_text": result[0]["generated_text"]}
