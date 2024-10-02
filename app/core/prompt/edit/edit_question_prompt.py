from langchain.prompts import PromptTemplate

edit_question_prompt = PromptTemplate(
    template="""
    ### Instructions
    1. Edit user survey data following prompt: {user_prompt}
    2. Reference existing survey data

    ### User Question
    {user_question}

    """,
    input_variables=["user_prompt", "user_question"])
