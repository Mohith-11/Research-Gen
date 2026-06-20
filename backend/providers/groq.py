from langchain_groq import ChatGroq
from config.settings import GROQ_API_KEY

groq_llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    api_key=GROQ_API_KEY
)