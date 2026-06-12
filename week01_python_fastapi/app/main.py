from fastapi import FastAPI
from app.schemas import ChatRequest,ChatResponse
from app.services import fake_llm_generate,build_prompt,estimate_tokens


app = FastAPI(title="Week 01 LLM API Demo")

@app.get("/")
def root():
    return {"message": "Welcome to the Week 01 LLM API Demo"}

@app.post("/chat", response_model=ChatResponse)
        # response_model = ChatResponse 表示返回的数据类型是 ChatResponse
def chat(chat_request: ChatRequest):
    try:
        prompt = build_prompt(chat_request.question)
        answer = fake_llm_generate(prompt)
        token_count = estimate_tokens(prompt)
        return ChatResponse(answer=answer, token_count=token_count,model="fake-llm-v1")
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))    