from langchain.prompts import PromptTemplate
from app.core.prompt.prompt_injection_block_prompt import prompt_injection_block_prompt


survey_question_creation_prompt = PromptTemplate(
    template=prompt_injection_block_prompt
    + """
    You are a question creator that creates a suitable number of questions based on user prompts:{user_prompt}
    Create question based on the survey basic and section materials below.

    ### Survey Basic and Section Materials
    {survey_basic_and_section_content}

    ### Creation Requirements
    1. {user_prompt} (e.g., Include questions on a specific topic.)
    2. Use Mostly Closed-Ended Questions
    3. Avoid Leading Questions
        ex) ask “How helpful were our customer service representatives?” instead of “How helpful were our friendly customer service representatives?”
    4. Balance Response Options : Provide a symmetrical range of response choices to capture genuine feedback
        ex)
        a. Very helpful  
        b. Helpful  
        c. Neutral  
        d. Unhelpful  
        e. Not helpful at all
    5. Use Precise Language : Avoid absolute terms like “always” or “never” that force binary answers. 
    6. Avoid Double-Barreled Questions : Ask about one topic at a time to prevent confusion. 
        ex) Instead of “Rate the quality of our products and support,”
        split into:
        - “Rate the quality of our products.”
        - “Rate the quality of our support.”
    7. if other choice exits, set isAllowOtherChoice to True
    8. if the question is required, set isRequired to True
    9. Do not create too few questions (fewer than 6).

    ### output(Korean)
    #### Questions
    ##### Section: The section to which the question belongs
    ##### Question Type: SINGLE_CHOICE(allow only one choice) / MULTIPLE_CHOICE(allow multiple choices) / TEXT_RESPONSE(text response)
    ##### Title : Question's title
    ##### Choices: Question's choice
    ##### isAllowOtherChoice: True / False
    ##### isRequired: True / False
    """,
    input_variables=["user_prompt", "survey_basic_and_section_content"],
)
