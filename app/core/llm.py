import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from typing import Optional
from dotenv import load_dotenv
load_dotenv()

def get_llm(provider="groq", model: Optional[str] = None, temperature=0.7, streaming: bool = False):
    provider = provider.strip().lower()

    if provider == "gemini":
        return ChatGoogleGenerativeAI(
            model="gemini-2.0-flash-lite",
            temperature=temperature,
            streaming=streaming,
            api_key=os.getenv("GOOGLE_API_KEY"),
        )

    elif provider == "groq":
        return ChatGroq(
            model="llama-3.1-8b-instant",
            temperature=temperature,
            streaming=streaming,
            groq_api_key=os.getenv("GROQ_API_KEY"),
        )
    else:
        raise ValueError(f"Invalid provider: {provider}")
