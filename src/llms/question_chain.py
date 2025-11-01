from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from llms.get_llm import get_llm_client


SYSTEM_PROMPT = """
Generate Question 1
"""

def get_question(overview):
    llm = get_llm_client("openai", "gpt-4.1-nano")
    questions=(
        overview
        | PromptTemplate.from_template(SYSTEM_PROMPT + "{overview}") 
        | llm 
        | StrOutputParser()
    )

    return questions