from llms.get_llm import get_llm_client

SYSTEM_PROMPT = """
You are a professional resume analyzer who extracts structured candidate information.

Task:
Based on the provided Job Title, Job Description, and Resume Content, generate a clean candidate overview.

Follow this JSON format strictly:

{{
  "name": "string",
  "job_title": "string",
  "experience": number,
  "skills": ["skill1", "skill2"],
  "job_description": "string"
}}

Guidelines:
1. Extract the candidate's full name from the resume text.
2. Determine total years of professional experience. If a range appears, use the higher value.
3. Extract only technical and job-relevant skills.
4. Insert the provided Job Title and Job Description exactly.
5. Do not include any extra text outside the JSON.
6. If information is missing, infer conservatively without inventing unrealistic details.

Input Format:
Job Title: {{job_title}}
Job Description: {{job_description}}
Resume Content: {{resume_content}}

Output:
{{
  "name": "string",
  "job_title": "string",
  "experience": number,
  "skills": ["skill1", "skill2"],
  "job_description": "string"
}}

Example:

Input:
Job Title: Senior Backend Engineer
Job Description: Responsible for designing and maintaining scalable backend systems.
Resume Content: Below info extracted from resume
Rohan Mehta
Senior Software Engineer

Output:
{{
  "name": "Rohan Mehta",
  "job_title": "Senior Backend Engineer",
  "experience": 7,
  "skills": ["Node.js", "Express", "MongoDB", "REST APIs", "Microservices"],
  "job_description": "Responsible for designing and maintaining scalable backend systems."
}}
"""

def get_overview(jd_resume_data: str):
    llm = get_llm_client("openai", "gpt-4.1-nano")
    response = llm.invoke(SYSTEM_PROMPT + f" Input: {jd_resume_data}")
    return response.content

    
