import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

chatbot = pipeline("text-generation", model="gpt2")


class ChatRequest(BaseModel):
    message: str
    history: list[list[str]] = [[]]


@app.post("/chat/")
async def chat(chat_request: ChatRequest):
    if not chat_request.message:
        raise HTTPException(status_code=400, detail="Message cannot be empty")
    response = chatbot(chat_request.message, max_length=100)
    return {"response": response[0]["generated_text"]}


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI new2!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
