from llms.overview_chain import get_overview
from llms.question_chain import get_question

from dotenv import load_dotenv

load_dotenv()

def generate_interview_questions(jd_resume_data):
    overview = get_overview(jd_resume_data)
    questions = get_question(overview)
    return questions