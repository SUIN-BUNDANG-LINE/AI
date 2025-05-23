from langchain.prompts import PromptTemplate


edit_survey_prompt = PromptTemplate(
    template="""
    You are a survey editor.    
    Edit the user survey: {user_survey_data} according the user prompt: {user_prompt}
    Prioritize the user prompt over the content rules below.
    
    ## Rules
    ### ID Rules when remain
    You should not edit the ids.

    ### ID Rules when edit
    You should not edit the ids.

    ### ID Rules when create
    - You should not make your own.
    - Instead making ids, just set them null
    
     ### Format Rules
    - id: Unique identifier or null(not "null")
    - title
        - Title of the survey
        - Create a survey title based on the reference materials ended with "~에 대한 조사" (e.g., 설문 제작 및 참여에 대한 경험 조사)
    - description: Description of the section
    - finish_message: Message displayed upon completion of the survey
    - sections: Sections of the survey
        - id: Unique identifier or null(not "null")
        - title: Title of the section
        - description: Description of the section
        - questions: Questions included in the section
            - id: Unique identifier or null(not "null")
            - question_type: Type of the question: SINGLE_CHOICE, MULTIPLE_CHOICE, TEXT_RESPONSE
            - title: Title of the question
            - description: Description of the question
            - is_required: Indicates whether answering the question is mandatory or not
            - choices: Options for choice question
            - is_allow_other: 
            - Indicates whether allow users to input their own answers directly, even for questions where they select from given options or not
            - Set is_allow_other to false when QUESTION_TYPE is TEXT_RESPONSE
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
            - Else, Set is_allow_other to false
    - reason
        - Explain in detail how the user prompt was implemented.
        - Respond same as user prompt language.
        
    ### Content Rules of sections
    - Create sections based on the reference materials that become key themes in structuring the survey questions.
    - If you need to delete section set it empty list. Keep others intact.

    ### Content Rules of questions
    - Determine the QUESTION TYPE. Create question below types:
        - SINGLE_CHOICE: Create questions that ask for a single answer choice.
        - MULTIPLE_CHOICE: Create questions that ask for multiple answer choices.
        - TEXT_RESPONSE: Create questions that ask for a text response.
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
    input_variables=["user_prompt", "user_survey_data"],
)
