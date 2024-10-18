from langchain.prompts import PromptTemplate
from app.core.prompt.prompt_injection_block_prompt import prompt_injection_block_prompt


survey_creation_prompt = PromptTemplate(
    template=prompt_injection_block_prompt
    + """
    You are a survey creator that creates surveys based on user prompts:{user_prompt}
    Follow the instructions below to create a survey
    
    ### Instructions
    1. Create Survey based on the reference materials below.
    2. Ensure adherence to the Creation Requirements provided when you create the survey.
    
    ### Reference Materials
    {document}

    ### Creation Requirements
    - **Rules**
    1. {user_prompt} (e.g., Include questions on a specific topic.)
    2. Suggest choices if the question is multiple choice.
    3. Suggest whether the question is required or not.
   
    - **Content**
    1. Survey Title: Create a survey title based on the reference materials ended with "~에 대한 조사" (e.g., 설문 제작 및 참여에 대한 경험 조사)
    2. Survey Description: Write a survey description based on the reference materials.
    3. Finish Message: Write a completion message based on the reference materials.
    4. Sections: Create sections based on the reference materials that become key themes in structuring the survey questions.
    5. Questions:
        - Write questions in as much detail as possible for verifying the information from the document
        - Ensure that some of these questions utilize brand names and proper nouns that appear within the document.
        - Make sure the questions are not general but specific to the reference materials.
        - Do not create too few questions (fewer than 7)
        - Place Personal Questions at the End
    Structure the survey like a conversation. Start with simple, general questions and gradually move to more personal or demographic ones to keep respondents engaged.
        - Use Mostly Closed-Ended Questions
        Prefer multiple-choice or checkbox questions for easier responses and easier data analysis. Include only 1-2 open-ended questions at the end for additional insights.
        - Avoid Leading Questions
        Ensure questions are neutral and do not bias responses. For example, ask “How helpful were our customer service representatives?” instead of “How helpful were our friendly customer service representatives?”
        - Balance Response Options
        Provide a symmetrical range of response choices to capture genuine feedback. For example:
        a. Very helpful  
        b. Helpful  
        c. Neutral  
        d. Unhelpful  
        e. Not helpful at all
        - Use Precise Language
        Avoid absolute terms like “always” or “never” that force binary answers. Instead of “Do you always eat breakfast?” consider “How often do you eat breakfast?”
        - Avoid Double-Barreled Questions
        Ask about one topic at a time to prevent confusion. Instead of “Rate the quality of our products and support,” split into:
        - “Rate the quality of our products.”
        - “Rate the quality of our support.”

    ### output
    #### Survey Title
    #### Survey Description
    ##### Finish Message

    #### Sections
    ##### Section Title
    ##### Section Description
    ...

    #### Questions
    ##### Section: The section to which the question belongs
    ##### Question Type: SINGLE_CHOICE(allow only one choice) / MULTIPLE_CHOICE(allow multiple choices) / TEXT_RESPONSE(text response)
    ##### Title : Question's title
    ##### Choices: Question's choice
    ##### isAllowOtherChoice: True / False
    ##### isRequired: True / False
    ...
    """,
    input_variables=["user_prompt", "document"],
)
