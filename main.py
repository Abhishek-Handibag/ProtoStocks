# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Pydantic model for request/response
class Item(BaseModel):
	name: str
	description: Optional[str] = None
	price: float
	tax: Optional[float] = None

@app.get("/")
def read_root():
	return {"message": "Welcome to ProtoStocks FastAPI backend!"}

@app.post("/items/", response_model=Item)
def create_item(item: Item):
	return item
