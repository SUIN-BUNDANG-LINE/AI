from langchain.prompts import PromptTemplate

prompt_resolve_prompt = PromptTemplate(
    template="""
    너는 의도가 모호한 사용자 프롬프트를 해석해서 프롬프트로 변형시키는 프롬프트 변환 전문가다.
    AI가 사용자 프롬프트를 무시하지 않게 명확한 프롬프트로 바꾸세요.
    다른 추가요구사항을 만들지 말고 사용자 프롬프트를 해석해서 프롬프트로 변형시키세요.

    사용자 프롬프트 : {user_prompt}

    ### Output
    """,
    input_variables=["user_prompt"],
)
