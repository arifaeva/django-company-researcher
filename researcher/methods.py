from pydantic import BaseModel

from core.prompt_manager import PromptManager
from researcher.prompts import QUERY_GENERATOR_PROMPT, BUSINESS_PROFILE_PROMPT
from researcher.utils import tavily_client


class Queries(BaseModel):
    category: str
    queries: list[str]

def generate_queries(category, company_name):
    pm = PromptManager()
    pm.add_message("system", QUERY_GENERATOR_PROMPT.format(company_name=company_name, category=category))
    pm.add_message("user", "")
    return pm.generate_structure(Queries)

def research(query):
    response = tavily_client.qna_search(query)
    return response

def generate_business_profile(context):
    pm = PromptManager()
    pm.add_message("system", BUSINESS_PROFILE_PROMPT)
    pm.add_message("user", f"Generate a business profile for company based on the following context: {context}")
    return pm.generate()