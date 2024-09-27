from langchain.prompts import PromptTemplate
from app.core.prompt.prompt_injection_block_prompt import prompt_injection_block_prompt

edit_question_prompt = PromptTemplate(
    prompt="""
    {prompt_injection_block_prompt}

    ### Instructions
    1. {user_prompt}
    2. Refence the Reference
    
    ### Referece
    1. {user_survey_data}
    2. {prototype_survey_data}

    """,
    input=["user_prompt", "user_survey_data", "prototype_survey_data"]
)