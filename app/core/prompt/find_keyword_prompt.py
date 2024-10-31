from langchain.prompts import PromptTemplate

find_keyword_prompt = PromptTemplate(
    template="""
    사용자 명령에서 ai가 모를 가능성이 높은 단어 또는 표현을 검색할 키워드로 제공하려고 합니다.
    너는 인터넷 검색을 위해 검색이 잘 될 것 같은 키워드를 딱 하나 제공해야한다.

    ### 사용자 명령
    {user_instruction}

    ### 키워드 추출 규칙
    - 설문조사 관련 단어는 포함하지 마세요.
    - 검색이 필요 없다면 "NOT_TO_NEED_SEARCH"를 출력하세요
    - 검색이 필요 하다면 키워드는 사용자 프롬프트에 주어진 단어들로만 조합해서 만드시오.

    ### Output
    -
    """,
    input_variables=["user_instruction"],
)
