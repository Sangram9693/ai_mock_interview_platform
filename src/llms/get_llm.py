from langchain_core.language_models.chat_models import BaseChatModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

def get_llm_client(provider: str, model_name: str) -> BaseChatModel:
    """
        Takes Provider - gemini or openai
        Model name - takes model name wrt provider

        Return the chat object of provider
    """
    if "gemini" in provider.lower():
        return ChatGoogleGenerativeAI(model=model_name)
    
    if "openai" in provider.lower():
        return ChatOpenAI(model=model_name)
    
    else:
        return ValueError(f"Unkown LLM provider or model")
    

