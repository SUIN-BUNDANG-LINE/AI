from langchain.prompts import PromptTemplate
from app.core.prompt.prompt_injection_block_prompt import prompt_injection_block_prompt

survey_basic_and_section_creation_prompt = PromptTemplate(
    template=prompt_injection_block_prompt
    + """
    Create Survey basic info and section based on the reference materials below to use making questions
    
    ### Reference Materials
    {document}

    ### Creation Requirements
    1. Survey Title: Create a survey title based on the reference materials ended with "~에 대한 조사" (e.g., 설문 제작 및 참여에 대한 경험 조사)
    2. Section Description: Describe in one sentence what this section will investigate
    3. Sections
    1) Divide it into several major topics.
    2) Define precise objectives for your survey.
        ex) Instead of aiming to “understand customer satisfaction,” specify “identify key factors causing customer churn.” Clear goals help prioritize essential questions.
    3) Place Section that contains Personal Questions at the End
    4) Structure like a conversation. Start with simple, general questions and gradually move to more personal or demographic ones to keep respondents engaged.

    ### output
    #### Survey Title
    #### Survey Description
    ##### Finish Message

    #### Sections
    ##### Section Title
    ##### Section Description
    """,
    input_variables=["user_prompt", "document"],
)
