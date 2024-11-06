from langchain.prompts import PromptTemplate


find_keyword_prompt = PromptTemplate(
    template="""
    user prompt에는 AI가 모르는 정보가 포함되어 있을 수 있습니다.
    따라서 검색을 위해 user prompt에서 키워드를 추출하고자합니다.
    키워드를 출력해주세요.
    명령형 키워드는 추출하지마세요
    ex) ~해줘
    최대 5개 만드세요.
    
    ### User Prompt
    {user_prompt}
    
    ### Output
    -
    """,
    input_variables=["user_prompt"],
)
