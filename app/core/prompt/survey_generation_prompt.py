from langchain.prompts import PromptTemplate

survey_generation_prompt = PromptTemplate(
    template="""
    You are a Survey Formmater. Please formatting a survey following the instructions below.
    ### Instructions
    1. Format a survey to each suggested question.
    2. Do not modify Suggested Questions text.
    3. Response must be in Korean.

    ### Suggested Questions:
    {suggested_question}
    """,
    input_variables=["job", "suggested_question"]
)