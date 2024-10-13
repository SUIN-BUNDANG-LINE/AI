from langchain.prompts import PromptTemplate
from app.core.prompt.prompt_injection_block_prompt import prompt_injection_block_prompt

edit_question_prompt = PromptTemplate(
    template=prompt_injection_block_prompt
    + """
    You are a survey editor that edit user question, which is part of the section, based on user prompts:{user_prompt}
    Follow the instructions below to edit a question
    
    ### User question
    {user_survey_data}
    
    ### Instructions
    1. Reference the document summation below to edit the question
    2. Ensure adherence to the Creation Requirements provided when you edit the question.
    
     ### Creation Requirements
    - **Rules**
    1. {user_prompt} (e.g., Include questions on a specific topic.)
    2. Suggest choices if the question is multiple choice.
    3. Suggest whether the question is required or not.
    4. Keep id or set id null
    - **Content**
    1. Questions
        
    ### output
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
