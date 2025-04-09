from langchain.prompts import PromptTemplate

find_keyword_prompt = PromptTemplate(
    template="""
    ## 요구 사항
    user prompt에는 AI가 모르는 정보가 포함되어 있을 수 있습니다.
    따라서 검색을 위해 user prompt에서 키워드를 추출하고자합니다.
    키워드들을 개행문자로 구분하여 출력해주세요.
    ### User Prompt
    {user_prompt}
    
    ## 제약 사항
    1. 명령형 키워드는 추출하지마세요: ex) ~해줘
    2. 최대한도는 5개입니다
    
    ## Output
    
    """,
    input_variables=["user_prompt"],
)
