from langchain_google_genai import ChatGoogleGenerativeAI
from config.settings import GOOGLE_API_KEY

gemini_llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    google_api_key=GOOGLE_API_KEY
)