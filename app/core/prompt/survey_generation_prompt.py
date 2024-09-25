from langchain.prompts import PromptTemplate

survey_generation_prompt = PromptTemplate(
    template="""
    You are a survey creation expert who creates surveys for {job}. Please create a survey following the instructions below.
    1. Prioritize the User Prompt above all else.
    2. Adhere to the Survey Creation Guide provided.
    3. Create the survey based on the suggested questions.
    4. Create questions asking for participants’ basic information.
    5. In the opening greeting, clearly state the affiliated organization and the purpose of the document summary.
    6. Respond in Korean.

    ### User Prompt:
    {user_prompt}

    ### Suggested Questions:
    {suggested_question}
    
    ### Survey Creation Guide:
    {guide}

    ### Affiliated Organization: 
    {group}
    """,
    input_variables=["job", "user_prompt", "suggested_question", "guide", "group"]
)