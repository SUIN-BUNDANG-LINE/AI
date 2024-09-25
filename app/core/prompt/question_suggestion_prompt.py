from langchain.prompts import PromptTemplate

question_suggestion_prompt = PromptTemplate(
    template="""
    Summarize the reference materials according to the suggestion requirements.

    ### Reference Materials
    {document}

    ### Suggestion Requirements
    - **Format**: Enumerated list
    - **Content**
    1. Suggestions survey questions as much detail as possible for verifying the information from the document.
    2. Suggestions relevant survey questions based on reference materials.
    """,
    input_variables=["document"]
)