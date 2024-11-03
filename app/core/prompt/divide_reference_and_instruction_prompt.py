from langchain.prompts import PromptTemplate


divide_reference_and_instruction_prompt = PromptTemplate(
    template="""
    사용자 프롬프트에는 단순한 참고 문서와 사용자 명령이 포함되어 있습니다.
    이를 나누어 사용자 명령을 찾아 그대로 출력하세요.
    사용자 명령은 명령형입니다.
    수정하려는 것인지 무엇인지도 출력하세요
    
    ### 사용자 프롬프트
    {user_prompt}

    ### Output
    - 사용자 명령:
    - 수정 대상: 
    """,
    input_variables=["user_prompt"],
)
