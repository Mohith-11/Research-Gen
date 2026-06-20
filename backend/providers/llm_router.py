from groq import RateLimitError

from providers.groq import groq_llm
from providers.gemini import gemini_llm
from providers.openrouter import openrouter_llm


def invoke_llm(prompt):

    # Try Groq
    try:
        print("Using Groq...")
        return groq_llm.invoke(prompt)

    except RateLimitError:
        print("Groq quota exceeded. Switching to Gemini...")

    except Exception as e:
        print(f"Groq Error: {e}")
        print("Trying Gemini...")

    # Try Gemini
    try:
        print("Using Gemini...")
        return gemini_llm.invoke(prompt)

    except Exception as e:
        print(f"Gemini Error: {e}")
        print("Trying OpenRouter...")

    # Try OpenRouter
    try:
        print("Using OpenRouter...")
        return openrouter_llm.invoke(prompt)

    except Exception as e:
        print(f"OpenRouter Error: {e}")

    raise Exception("All LLM providers failed.")