from langchain.prompts import PromptTemplate

survey_parsing_prompt = PromptTemplate(template="""
    You are a Survey Formmater. Please formatting a survey following the instructions below.
    ### Instructions
    1. Format a survey to each suggested question.
    2. Do not appear quesition choice if it is Other choice. 
    3. Do not modify Suggested Questions text.
    4. Response must be in Korean.

    ### Suggested Questions:
    {suggested_question}
    """,
                                       input_variables=["suggested_question"])
