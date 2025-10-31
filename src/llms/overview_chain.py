from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from llms.get_llm import get_llm_client


SYSTEM_PROMPT = """
Generate overview of given input in 5 words
"""

def get_overview():
    llm = get_llm_client("openai", "gpt-4.1-nano")
    overview = (
        PromptTemplate.from_template(SYSTEM_PROMPT + "{input_text}") 
        | llm 
        | StrOutputParser()
    )
    return overview