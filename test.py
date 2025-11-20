from llm import llm_by_agent


for chunk in llm_by_agent.stream("你是谁？"):
    if chunk.additional_kwargs.get("reasoning_content"):
        print(chunk.additional_kwargs.get("reasoning_content"), end="", flush=True)
    else:
        print(chunk.text, end="", flush=True)