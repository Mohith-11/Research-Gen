from langchain_openai import ChatOpenAI
from config.settings import OPENROUTER_API_KEY

openrouter_llm = ChatOpenAI(
    model="meta-llama/llama-3.3-70b-instruct",
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
    temperature=0
)