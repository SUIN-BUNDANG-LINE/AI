from langchain.prompts import PromptTemplate


divide_reference_and_instruction_prompt = PromptTemplate(
    template="""
    사용자 프롬프트에는 단순한 참고 문서와 사용자 요청 문장이 포함되어 있습니다.
    이를 나누어 사용자 요청 문장을 찾아 그대로 출력하세요.
    사용자 요청 문장은 명령형입니다.
    
    ### 사용자 프롬프트
    {user_prompt}

    ### Output
    -
    """,
    input_variables=["user_prompt"],
)
