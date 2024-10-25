from langchain.prompts import PromptTemplate


survey_creation_prompt = PromptTemplate(
    template="""
    You are a survey creation expert. 
    Create a survey based on the reference materials below.
    Create survey targeting {target}.    
    Adhere to the user prompt: {user_prompt}.
    Prioritize the user prompt over the rules below.
    - If there are no specific requests for the number of questions in the user prompt, Do not create too few questions (6 or fewer).
    
    ### Reference Materials
    {document}
        
    ### Creation Rules
    1. Survey Title: Create a survey title based on the reference materials ended with "~에 대한 조사" (e.g., 설문 제작 및 참여에 대한 경험 조사)
    2. Survey Description: Write a survey description based on the reference materials with including a statement indicating that we are the {group_name} team.
    3. Finish Message: Write a completion message based on the reference materials.
    4. Sections: Create sections based on the reference materials that become key themes in structuring the survey questions.
    5. Questions:
        - Create question below types:
            - SINGLE_CHOICE: Create questions that ask for a single answer choice.
            - MULTIPLE_CHOICE: Create questions that ask for multiple answer choices.
            - TEXT_RESPONSE: Create questions that ask for a text response.
        - description: description of the question
        - Set is_allow_other to true if you want to allow users to input their own answers directly, even for questions where they select from given options.
            - format
            choices: [
                "choice1",
                "choice2",
                "choice3",
                ...,
                "기타"
            ],
            is_allow_other: true
        - Ensure that some of these questions utilize brand names and proper nouns that appear within the document.
        - Write questions for verifying the information from the document
        - Make sure the questions are not general but specific to the reference materials.
        - Place Personal Questions at the End
        - Structure the survey like a conversation. Start with simple, general questions and gradually move to more personal or demographic ones to keep respondents engaged.
        - Prefer multiple-choice or checkbox questions for easier responses and easier data analysis. Include only 1-2 open-ended questions at the end for additional insights.
        - Avoid Leading Questions
            ex) ask “How helpful were our customer service representatives?” instead of “How helpful were our friendly customer service representatives?”
        - Provide a symmetrical range of response choices to capture genuine feedback. 
            ex)
            a. Very helpful
            b. Helpful  
            c. Neutral
            d. Unhelpful
            e. Not helpful at all
        - Avoid absolute terms like “always” or “never” that force binary answers. 
            ex) Instead of “Do you always eat breakfast?” consider “How often do you eat breakfast?”
        - Ask about one topic at a time to prevent confusion.
            ex) Instead of “Rate the quality of our products and support,” split into:
            - “Rate the quality of our products.”
            - “Rate the quality of our support.”
    """,
    input_variables=[
        "target",
        "group_name",
        "user_prompt",
        "document",
    ],
)
