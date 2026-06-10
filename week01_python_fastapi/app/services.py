# 该文件负责模拟大模型的回答



def build_prompt(question:str) ->str:
    # 一般在真实开发中，不会直接将用户的问题丢给大模型，而是会加上一些系统的提示词来约束模型的行为！
    return f"please use slowly and accuracy to answer the following question: {question}"

def fake_llm_generate(prompt:str) ->str:
    # 这里可以调用实际的 LLM API 或者使用一些简单的规则来生成回答
    return f"this is an answer to the question '{prompt}'."

def estimate_tokens(prompt:str) ->int:
    # 简单的估算方法，实际应用中可能需要更复杂的逻辑
    return len(prompt) // 2