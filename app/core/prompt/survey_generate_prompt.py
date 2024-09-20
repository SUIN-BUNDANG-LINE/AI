from langchain.prompts import PromptTemplate

summation_prompt = PromptTemplate(
    template="""
    Please summarize the reference materials according to the summary requirements.

    ### Reference Materials
    {document}

    ### Summary Requirements
    - **Format**: Enumerated list
    - **Content**
    1. seems to require verification from the document
    2. Suggest relevant survey questions based on reference materials
    """,
    input_variables=["document"]
)

instruct_prompt = PromptTemplate(
    template="""
    You are a survey creation expert who creates surveys for {who}. Please create a survey following the instructions below.
    1. Create the survey based on the document summary.
    2. Adhere to the User Prompt provided.
    3. In the opening greeting, clearly state the affiliated organization and the purpose of the document summary.
    4. Must be written in Korean.
    5. Adhere to the Survey Creation Guide provided.
    
    ### User Prompt:
    {user_prompt}

    ### Document Summary:
    {summation}

    ### Survey Creation Guide:
    {guide}

    ### Affiliated Organization: 
    {group}

    """,
    input_variables=["who", "user_prompt", "summation",  "guide", "group"]
)