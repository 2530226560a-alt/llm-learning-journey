# 该文件负责定义响应请求和请求格式

from pydantic import BaseModel


class ChatRequest(BaseModel):
    question:str
    user_id:str | None = None


class ChatResponse(BaseModel):
    answer:str
    model:str 
    tokens_used:int
  