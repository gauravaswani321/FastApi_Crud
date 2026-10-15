from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello"}

@app.get("/items/{itemId}")
def get_item(itemId: int):
    return {"itemId": itemId}