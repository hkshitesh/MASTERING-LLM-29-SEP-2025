from fastapi import FastAPI
from pydantic import BaseModel
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import base64
import io

app = FastAPI()
model = load_model("app/cnn_model.h5")

class ImageInput(BaseModel):
    image_base64: str

@app.post("/predict/")
def predict(data: ImageInput):
    image = Image.open(io.BytesIO(base64.b64decode(data.image_base64))).convert("L")
    image = image.resize((28, 28))
    image = np.array(image).reshape(1, 28, 28, 1).astype("float32") / 255
    prediction = model.predict(image)
    pred_class = int(np.argmax(prediction))
    return {"prediction": pred_class}
