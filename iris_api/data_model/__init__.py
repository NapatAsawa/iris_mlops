from pydantic import BaseModel
from typing import List

# Define the expected input schema
class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

class IrisBatchRequest(BaseModel):
    data: List[IrisFeatures]  # Accepts multiple records