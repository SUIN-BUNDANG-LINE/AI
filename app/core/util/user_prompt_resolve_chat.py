from app.core.util.function_execution_time_measurer import FunctionExecutionTimeMeasurer
from app.core.prompt.prompt_resolve_prompt import prompt_resolve_prompt


def chat_resolve_user_prompt(ai_manager, user_prompt):
    if user_prompt == "":
        return

    prompt = prompt_resolve_prompt.format(user_prompt=user_prompt)

    new_user_prompt = FunctionExecutionTimeMeasurer.run_function(
        "사용자 프롬프트 명확화 태스크", ai_manager.chat, prompt
    )

    print(new_user_prompt)

    return new_user_prompt
