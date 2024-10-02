from langchain.prompts import PromptTemplate

edit_total_survey_prompt = PromptTemplate(
    template="""
    ### Instructions
    1. Edit user survey data following prompt: {user_prompt}
    2. Reference existing survey data
    3. Do not appear quesition choice if it is Other choice. 

    ### User Survey Data
    1. {user_survey_data}

    """,
    input_variables=["user_prompt", "user_survey_data"])
