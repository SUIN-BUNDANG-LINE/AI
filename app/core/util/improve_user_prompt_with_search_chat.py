from langchain_community.tools import DuckDuckGoSearchRun

from app.core.util.ai_manager import AIManager
from app.core.prompt.divide_reference_and_instruction_prompt import (
    divide_reference_and_instruction_prompt,
)
from app.core.prompt.find_keyword_prompt import find_keyword_prompt


def chat_improve_user_prompt_with_search(ai_manager: AIManager, user_prompt):
    if user_prompt == "":
        return

    user_instruction = ai_manager.chat(
        divide_reference_and_instruction_prompt.format(user_prompt=user_prompt)
    )

    print(f"user_instruction: {user_instruction}")

    keyword = ai_manager.chat(
        find_keyword_prompt.format(user_instruction=user_instruction)
    )

    if keyword == '""':
        return user_prompt

    print(f"keyword: {keyword}")

    search = DuckDuckGoSearchRun()

    searched_result = search.invoke(keyword)

    print(f"searched_result: {searched_result}")

    result = user_prompt + " reference) " + searched_result
    print(f"result: {result}")
    return result
