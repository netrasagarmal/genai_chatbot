from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

from chatbot import get_llm_answer

app = FastAPI()

# Define a BaseModel for request/response data
class RequestBody(BaseModel):
    question: str
    max_output_tokens : int = 1
    temperature:float = 0.0
    top_p : float = 0.50
    top_k : int = 50
    penealty : float= 0.0

@app.post("/chat")
async def create_item(request: RequestBody)->dict:

    llm_response = await get_llm_answer(question = request.question,
                                        max_output_tokens = request.max_output_tokens,
                                        temperature = request.temperature,
                                        top_p = request.top_p,
                                        top_k = request.top_k,
                                        penealty = request.penealty)
    
    return {"response": llm_response}

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI!"}

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True, log_level="debug")
