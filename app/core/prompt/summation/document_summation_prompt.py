from langchain.prompts import PromptTemplate

document_summation_prompt = PromptTemplate(
    template="""
    Summarize user document as detail as possible in the document summation that contains content

    ### User Document
    {user_document}

    ### Document Summation
    """,
    input_variables=["user_document"],
)
