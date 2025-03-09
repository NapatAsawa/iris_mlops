from fastapi import FastAPI
import joblib
import os
from data_model import IrisBatchRequest
from loguru import logger
from config import MODEL_PATH

# Load the model
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")
model = joblib.load(MODEL_PATH)
logger.info("model loaded")
app = FastAPI()

@app.get("/healthcheck")
def healthcheck():
    return {"status": "ok"}

@app.post("/predict")
def predict(request: IrisBatchRequest):
    input_data = [[
        sample.sepal_length, 
        sample.sepal_width, 
        sample.petal_length, 
        sample.petal_width
    ] for sample in request.data]

    predictions = model.predict(input_data)
    return {"predictions": predictions.tolist()}