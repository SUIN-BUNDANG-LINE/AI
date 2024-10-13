from langchain.prompts import PromptTemplate
from app.core.prompt.prompt_injection_block_prompt import prompt_injection_block_prompt


survey_parsing_prompt = PromptTemplate(
    template=prompt_injection_block_prompt
    + """
    You are a Survey Formater. Please formatting the prototype survey following the instructions below.
    ### Instructions
    1. Do not appear question choice if it is Other choice.
    2. Do not modify Survey's text.
    3. Response must be in Korean.

    ### Prototype Survey
    {prototype_survey}
    """,
    input_variables=["prototype_survey"],
)
