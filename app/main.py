from typing import Union

from fastapi import FastAPI

from pydantic import BaseModel

class textmodel(BaseModel):
    text : str


app = FastAPI()

@app.get("/status")
def status():
    return "running"


@app.post("/chat")
def chat(model: textmodel):
    return model.text