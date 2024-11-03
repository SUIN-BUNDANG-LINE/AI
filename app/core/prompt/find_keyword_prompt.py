from langchain.prompts import PromptTemplate

find_keyword_prompt = PromptTemplate(
    template="""
    사용자 명령에서 ai가 모를 가능성이 높은 단어 또는 표현을 검색할 키워드로 제공하려고 합니다.
    너는 인터넷 검색을 위해 검색이 잘 될 것 같은 키워드를 딱 하나 제공해야한다.
    키워드 추출 규칙을 준수하세요.

    ### 사용자 명령
    {user_instruction}

    ### 키워드 추출 규칙
    - 질문을 만들어줘, 섹션을 만들어줘, 설문조사를 만들어줘 같은 명령은 제외하고 키워드를 추출해야 합니다.
    - 검색이 필요 없다면 "NOT_TO_NEED_SEARCH"를 출력하세요

    ### Output
    -
    """,
    input_variables=["user_instruction"],
)
