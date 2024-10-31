from langchain.prompts import PromptTemplate

find_keyword_prompt = PromptTemplate(
    template="""
    사용자 프롬프트에서 ai가 모를 가능성이 높은 단어 또는 표현을 검색할 키워드로 제공하려고 합니다.
    너는 인터넷 검색을 위해 검색이 잘 될 것 같은 키워드를 딱 하나 제공해야한다.

    ### 사용자 프롬프트
    {user_instruction}

    ### Instructions
    - 단순한 참고 문서와 사용자 요청 문장으로 나누세요
    - 사용자 요청 문장에서 키워드 추출 규칙을 참고하여 키워드만 추출한 뒤 출력하세요

    ### 키워드 추출 규칙
    - "선택지", "질문", "섹션", "설문지"와 같은 설문지 관련 단어는 포함하지 마세요.
    - 키워드는 사용자 프롬프트에 주어진 단어들로만 조합해서 만드시오.
    - 검색이 필요없다면 ""를 출력하세요

    ### Output
    - 키워드
    """,
    input_variables=["user_instruction"],
)
