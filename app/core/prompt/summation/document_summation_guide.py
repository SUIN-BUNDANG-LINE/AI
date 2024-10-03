from langchain.prompts import PromptTemplate

survey_creation_prompt = PromptTemplate(
    """
    Summarize user document as detail as possible in the document summation that contains cotent can be used for create questions.

    ### User Document
    {user_document}

    ### Document Summation
    """,
    input_variables=["user_document"],
)
