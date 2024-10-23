from langchain.prompts import PromptTemplate

prompt_resolve_prompt = PromptTemplate(
    template="""
    너는 사용자 프롬프트에서 요구하는 범위를 찾아내는 전문가이다.
        
    ### 사용자 프롬프트
    {user_prompt}
    
    ### 범위
    - 모든 내용
    - 섹션
        ex) 1번째 섹션
    - 질문
        ex) 1번째 질문
    
    ### 명령
    1. 사용자 프롬프트에서 범위를 찾아 출력하세요, 범위를 찾지 못하겠으면 범위를 모든 내용이라고 명시하세요.
    2. 사용자 요청에는 사용자 프롬프트를 그대로 작성하세요.

    ### Output
    사용자 요청:
    범위:
    """,
    input_variables=["user_prompt"],
)
