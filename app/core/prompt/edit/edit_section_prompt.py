from langchain.prompts import PromptTemplate

edit_section_prompt = PromptTemplate(
    template="""
    ### Instructions
    1. Edit user survey data following prompt: {user_prompt}
    2. Reference existing survey data
    3. questionType should be SINGLE_CHOICE(allow only one choice) / MULTIPLE_CHOICE(allow multiple choices) / TEXT_RESPONSE(text response)

    ### User Section
    {user_section}
    
    """,
    input_variables=["user_prompt", "user_section"],
)
