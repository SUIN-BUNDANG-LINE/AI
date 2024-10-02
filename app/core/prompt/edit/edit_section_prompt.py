from langchain.prompts import PromptTemplate

edit_section_prompt = PromptTemplate(
    template="""
    ### Instructions
    1. Edit user survey data following prompt: {user_prompt}
    2. Reference existing survey data

    ### User Section
    {user_section}
    
    """,
    input_variables=["user_prompt", "user_section"])
