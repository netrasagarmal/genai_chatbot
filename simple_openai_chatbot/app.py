from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

from chatbot import get_llm_answer

app = FastAPI()

# Define a BaseModel for request/response data
class RequestBody(BaseModel):
    question: str

@app.post("/chat")
async def create_item(request: RequestBody):

    llm_response = await get_llm_answer(question = request.question)
    
    return {"response": llm_response}

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI!"}

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True, log_level="debug")
