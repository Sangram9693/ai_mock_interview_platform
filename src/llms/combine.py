from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from operator import itemgetter 
from llms.overview_chain import get_overview
from llms.question_chain import get_question

from dotenv import load_dotenv

load_dotenv()

def generate_interview_questions(jd_resume_data):
    overview = get_overview()
    full_workflow = (
        {"overview": overview, "input_text": RunnablePassthrough()}
        | RunnableParallel(
            overview=itemgetter("overview"),
            questions=get_question(itemgetter("overview"))
        )
    )

    return full_workflow.invoke({"input_text": jd_resume_data})