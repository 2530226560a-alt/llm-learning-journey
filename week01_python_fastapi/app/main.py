from fastapi import FastAPI, HTTPException
import logging
from app.schemas import ChatRequest,ChatResponse
from app.services import fake_llm_generate,build_prompt,estimate_tokens


# 设置日志输出的门槛是Info，只有INFO、WARNING、ERROR、CRITICAL 级别的日志会被处理并输出，但是debug级别的不会
logging.basicConfig(level=logging.INFO)
# 创建一个 logger 对象，__name__ 代表当前模块的名字，例如：logger.info("消息")
logger = logging.getLogger(__name__)

app = FastAPI(title="Week 01 LLM API Demo")

@app.get("/")
def root():
    return {"message": "Welcome to the Week 01 LLM API Demo"}


@app.post("/chat", response_model=ChatResponse)
        # response_model = ChatResponse 表示返回的数据类型是 ChatResponse
def chat(chat_request: ChatRequest):
    try:
        logger.info(f"Received chat request: {chat_request}")

        prompt = build_prompt(chat_request.question)
        answer = fake_llm_generate(prompt)
        token_used = estimate_tokens(prompt + answer)

        logger.info(f"Generated answer: {answer} (tokens used: {token_used})")

        return ChatResponse(answer=answer, token_count=token_used,model="fake-llm-v1",prompt=prompt)
    except Exception as e:
            # 记录异常信息到日志中 
        logger.exception("Error processing chat request")    
            # 报错之后自定义状态码 500 ，并且detail中返回具体的报错信息
        return HTTPException(status_code=500, detail=str(e))    
