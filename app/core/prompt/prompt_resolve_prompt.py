from langchain.prompts import PromptTemplate

prompt_resolve_prompt = PromptTemplate(
    template="""
    너는 의도가 모호한 사용자 프롬프트를 해석해서 명확한 프롬프트로 변형시키는 프롬프트 변환 전문가다.
    명확한 프롬프트는 요청과, 범위 2가지로 이루어진다. 아래의 기록할 사항을 참조하세요
    
    ### 요청에 기록할 사항
    다른 추가요구사항을 만들지 말고 사용자 프롬프트를 해석해서 프롬프트로 변형시키세요.
    해석한 프롬프트를 명령에 명시하세요.
    
    ### 범위에 기록할 사항
    사용자 프롬프트에서 사용자가 지정한 범위를 찾아서 범위에 명시하세요.
    사용자가 별도의 범위를 명시하지 않았다면 범위를 전체라고 명시하세요.

    사용자 프롬프트: {user_prompt}

    ### Output
    요청:
    범위:
    """,
    input_variables=["user_prompt"],
)
