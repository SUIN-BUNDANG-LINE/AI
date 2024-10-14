from langchain.prompts import PromptTemplate
from app.core.prompt.prompt_injection_block_prompt import prompt_injection_block_prompt


edit_survey_prompt = PromptTemplate(
    template=prompt_injection_block_prompt
    + """
    You are a survey editor that edit user survey based on user prompts:{user_prompt}
    Follow the instructions below to edit a survey

    ### User Survey
    {user_survey_data}
    
    ### Instructions
    1. Reference the document summation below to edit the survey.
    2. Ensure adherence to the Creation Requirements provided when you edit the survey.
    
     ### Creation Requirements
    - **Rules**
    1. {user_prompt} (e.g., Include questions on a specific topic.)
    2. Suggest choices if the question is multiple choice.
    3. Suggest whether the question is required or not.
    4. Keep Survey Id, Section Id, Question Id or set them null if you want to create a new one.
    - **Content**
    1. Survey Title: Create a survey title based on the reference materials ended with "~에 대한 조사" (e.g., 설문 제작 및 참여에 대한 경험 조사)
    2. Survey Description: Write a survey description based on the reference materials.
    3. Finish Message: Write a completion message based on the reference materials.
    4. Sections
    5. Questions

    ### output
    #### Survey Id
    #### Survey Title
    #### Survey Description
    ##### Finish Message

    #### Sections
    ##### Section Id
    ##### Section Title
    ##### Section Description

    #### Questions
    ##### Question Id
    ##### Belonging Section: The section to which the question belongs
    ##### Question Type: SINGLE_CHOICE(allow only one choice) / MULTIPLE_CHOICE(allow multiple choices) / TEXT_RESPONSE(text response)
    ##### Title : Question's title
    ##### Choices: Question's choice
    ##### isAllowOtherChoice: True / False
    ##### isRequired: True / False
    """,
    input_variables=["user_prompt", "user_survey_data"],
)
