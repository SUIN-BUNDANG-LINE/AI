from langchain.prompts import PromptTemplate
from app.core.prompt.prompt_injection_block_prompt import prompt_injection_block_prompt

prompt_resolve_prompt = PromptTemplate(
    template="""
    너는 의도가 모호한 사용자 프롬프트를 해석해서 명확한 프롬프트로 변형시키는 프롬프트 변환 전문가다.
    프롬프트는 설문조사 제작에 사용된다.
    사용자가 대충 쓴 프롬프트를 정확히 수행하기 위해서, 제공된 프롬프트를 이해하고 복수의 단순한 프롬프트로 변환해야한다.
    프롬프트가 여러 의도를 담는 복합 프롬프트일 경우, 그 각각의 의도를 담는 단순한 프롬프트로 변환한다.
    단, and 조건일 경우 그 의미를 유지하세요
        ex)
        사용자 프롬프트 : 다중 선택 질문이고 기타 응답을 허용하는 질문을 만드세요
        잘못된 변형:
            1. 다중 선택 질문을 만들어 주세요.
            2. 기타 응답을 허용하는 질문을 만들어 주세요.
            3. ...
        옳은 변형:
            1. 다중 선택 질문을 만들어 주세요.
            2. 그 질문에는 기타 응답을 허용하세요
            3. 그 질문에는 ...

    사용자 프롬프트 : {user_prompt}

    ### Output
    하위 프롬프트:
    """,
    input_variables=["user_prompt"],
)
