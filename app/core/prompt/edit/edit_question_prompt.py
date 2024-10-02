from langchain.prompts import PromptTemplate

edit_question_prompt = PromptTemplate(
    template="""
    ### Instructions
    1. Edit user survey data following prompt: {user_prompt}
    2. Reference existing survey data
    3. Find the section in existing survey data based on the title key of user survey data and reference it
    4. Do not appear quesition choice if it is Other choice. 

    ### User Survey Data
    1. {user_survey_data}

    """,
    input_variables=["user_prompt", "user_survey_data"])
