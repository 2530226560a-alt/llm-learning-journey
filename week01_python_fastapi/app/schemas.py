# 该文件负责定义响应请求和请求格式

from pydantic import BaseModel
from pydantic import Field

# 表示的是请求的类型
class ChatRequest(BaseModel):
        # Field(...) 表示该字段是必填项
    question:str =Field(..., description="用户的问题",min_length=1,max_length=500 )
    user_id:str | None = None
    temperature:float = Field(default=0.5, description="生成文本的随机程度，取值范围为0-1，默认为0.5")

# 表示的是返回请求的数据类型
class ChatResponse(BaseModel):
    answer:str
    model:str 
    prompt:str
    tokens_used:int = 0
   