from langchain.prompts import PromptTemplate
from app.core.prompt.prompt_injection_block_prompt import prompt_injection_block_prompt

document_summation_prompt = PromptTemplate(
    template=prompt_injection_block_prompt
    + """
    Summarize user document as detail as possible in the document summation that contains content
    Include proper nouns such as brand names and personal names

    ### User Document
    {user_document}

    ### Document Summation
    """,
    input_variables=["user_document"],
)
