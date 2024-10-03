from langchain.prompts import PromptTemplate

edit_survey_prompt = PromptTemplate(
    template="""
    ### Instructions
    1. Edit user survey data following prompt: {user_prompt}
    2. Reference existing survey data

    ### User Survey
    {user_survey}

    """,
    input_variables=["user_prompt", "user_survey"],
)
