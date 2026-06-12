# 该文件负责定义响应请求和请求格式

from pydantic import BaseModel
from pydantic import Field


class ChatRequest(BaseModel):
        # Field(...) 表示该字段是必填项
    question:str =Field(..., description="用户的问题",min_length=1,max_length=500 )
    user_id:str | None = None


class ChatResponse(BaseModel):
    answer:str
    model:str 
    tokens_used:int = 0
  