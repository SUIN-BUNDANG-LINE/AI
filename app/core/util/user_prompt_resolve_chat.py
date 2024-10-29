from langchain_community.tools import DuckDuckGoSearchRun

from app.core.util.ai_manager import AIManager
from app.core.util.function_execution_time_measurer import FunctionExecutionTimeMeasurer
from app.core.prompt.prompt_resolve_prompt import prompt_resolve_prompt


def chat_resolve_user_prompt(ai_manager: AIManager, user_prompt):
    if user_prompt == "":
        return

    keyword = ai_manager.chat(prompt_resolve_prompt.format(user_prompt=user_prompt))

    search = DuckDuckGoSearchRun()

    searched_result = search.invoke(keyword)

    example = ai_manager.chat(
        f"""당신은 검색 결과를 활용하여 user prompt에 정보를 더해주는 전문가이다
        ai에게 정보를 전달하는 것이 목적이므로 그 역할에만 집중하세요
            ex) foo 정보로 설문조사를 만들어줘 : 직접 설문조사 예시를 만들지 말고 단순히 foo 정보를 나열하세요
        
        ### 검색 결과
        {searched_result}
        
        ### user prompt
        {user_prompt}
        
        ### Output
        -
        """
    )

    result = user_prompt + " ex) " + example
    return result
