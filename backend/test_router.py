from providers.llm_router import invoke_llm

response = invoke_llm("What is Agentic AI? Explain in 100 words.")

print(response.content)