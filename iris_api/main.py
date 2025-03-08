from fastapi import FastAPI
import joblib
import os
from data_model import IrisBatchRequest

model_path = "model/iris_model.pkl"

# Load the model
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found at {model_path}")
model = joblib.load(model_path)
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