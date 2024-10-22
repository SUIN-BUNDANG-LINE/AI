from langchain.prompts import PromptTemplate

document_summation_prompt = PromptTemplate(
    template="""
    Process the document to make it useful for the AI to generate surveys.
    Include proper nouns such as brand names and personal names

    ### User Document
    {user_document}

    ### Processed Document 
    """,
    input_variables=["user_document"],
)
