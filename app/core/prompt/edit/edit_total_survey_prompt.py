from langchain.prompts import PromptTemplate
from app.core.prompt.prompt_injection_block_prompt import prompt_injection_block_prompt

edit_total_survey_prompt = PromptTemplate(
    template="""
    ### Instructions
    1. Edit user survey data following prompt: {user_prompt}
    2. Your modified the survey data must harmonize with prototype survey data
    3. Refence the Reference

    ### User Survey Data
    1. {user_survey_data}

    """,
    input_variables=["user_prompt", "user_survey_data"]
)