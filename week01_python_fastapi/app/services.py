# 该文件负责模拟大模型的回答



def build_prompt(question:str) ->str:
    # 一般在真实开发中，不会直接将用户的问题丢给大模型，而是会加上一些系统的提示词来约束模型的行为！
    return (
        "你是我的人工智能助手，请根据用户的问题提供简洁、准确的回答。\n"
        f"用户的问题是：{question}\n"
        "回答："
    )

def fake_llm_generate(prompt:str,temperature:float = 0.7) ->str:
    # 这里可以调用实际的 LLM API 或者使用一些简单的规则来生成回答
    if "RAG" in prompt or "rag" in prompt.lower():
        return "RAG 是检索增强生成技术，它会先从外部知识库检索相关资料，再让大模型基于资料生成答案。"
    
    if "大语言模型" in prompt or "LLM" in prompt:
        return "大语言模型是基于海量文本训练的深度学习模型，能够理解和生成自然语言。"
    
    return f"this is a fake answer.   temperature = {temperature}"

def estimate_tokens(prompt:str) ->int:
    # 简单的估算方法，实际应用中可能需要更复杂的逻辑
    return len(prompt) // 2