from enum import Enum

from fastapi import FastAPI

# Enum Class
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

# Mock DB
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

app = FastAPI()

# Testing different types of endpoints

# Basic GET
@app.get("/")
async def root():
    return {"message": "Hello World!"}

# GET with a parameter
#@app.get("/items/{item_id}")
#async def read_item(item_id: int):
#    return {"item_id": item_id}

# GET with query parameters
@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

# GET using Enum
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW"}
    
    if model_name is ModelName.lenet:
        return { "model_name": model_name, "message": "LeCNN all the images"}
    
    return {"model_name": model_name, "message": "Have some residuals"}