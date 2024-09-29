from langchain.prompts import PromptTemplate
from app.core.prompt.prompt_injection_block_prompt import prompt_injection_block_prompt

survey_creation_prompt = PromptTemplate(
    template="""
    You are a survey creator that creates surveys based on user prompts:{user_prompt}
    
    Please create survey questions based on the reference materials below.
    ### Instructions
    1. Must adhere to the Survey Creation Guide provided when you suggest questions.
    2. Suggest Survey Title based on the reference materials ended with "~에 대한 조사"
    ex) 설문 제작 및 참여에 대한 경험 조사
    3. Suggest Survey Description based on the reference materials.
    4. Suggest Finish Message based on the reference materials.
    5. Suggest questions of reference materials according to the suggestion requirements.
    6. Summarize the document in the document summation section that contains cotent can be used for create questions.
    7. Response must be in Korean.
    
    ### Reference Materials
    {document}

    ### Survey Creation Guide:
    {guide}

    ### Suggestion Requirements
    - **Language**: Korean
    - **Format**: Enumerated list
    - **Rules**
    1. {user_prompt}
    2. Suggest choices if the question is multiple choice.
    3. Suggest whether the question is required or not.
    - **Content**
    1. Suggest sections based on the reference materials it becomes a key theme in structuring the questions of the survey.
    2. Survey questions as much detail as possible for verifying the information from the document that you think.
    3. Your suggested survey questions based on reference materials.
    - **Suggested Questions Format**
        section: Section to which the question belongs
        questionType: SINGLE_CHOICE(allow only one choice) / MULTIPLE_CHOICE(allow multiple choices) / TEXT_RESPONSE(text response)
        question: Suggested question's title
        choices: Suggested question's choice
        isAllowOtherChoice: True / False
        isRequired: True / False

    - output
    ### Suggested Survey Title

    ### Suggested Survey Description

    ### Suggested Finish Message

    ### Suggested Sections

    ### Suggested Questions

    ### Document Summation
    """,
    input_variables=["user_prompt", "document", "guide"]
)