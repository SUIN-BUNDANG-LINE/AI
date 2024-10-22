from langchain.prompts import PromptTemplate
from app.core.prompt.prompt_injection_block_prompt import prompt_injection_block_prompt

document_summation_prompt = PromptTemplate(
    template=prompt_injection_block_prompt
    + """
    Process the document to make it useful for the AI to generate surveys.
    Include proper nouns such as brand names and personal names

    ### User Document
    {user_document}

    ### Processed Document 
    """,
    input_variables=["user_document"],
)
