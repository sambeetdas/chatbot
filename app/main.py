from typing import Union

from fastapi import FastAPI

from pydantic import BaseModel

class textmodel(BaseModel):
    text : str


app = FastAPI()


@app.post("/chat")
def chat(model: textmodel):
    return model.text