from langchain_community.tools import DuckDuckGoSearchRun

from app.core.util.ai_manager import AIManager
from app.core.prompt.divide_reference_and_instruction_prompt import (
    divide_reference_and_instruction_prompt,
)
from app.core.prompt.find_keyword_prompt import find_keyword_prompt


NOT_TO_NEED_SEARCH_STRING = "NOT_TO_NEED_SEARCH"


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

    if keyword == NOT_TO_NEED_SEARCH_STRING:
        return user_prompt

    print(f"keyword: {keyword}")

    search = DuckDuckGoSearchRun()

    searched_result = search.invoke(keyword)

    print(f"searched_result: {searched_result}")

    result = user_instruction + " reference) " + searched_result
    print(f"result: {result}")
    return result


async def async_chat_improve_user_prompt_with_search(
    ai_manager: AIManager, user_prompt
):
    if user_prompt == "":
        return

    user_instruction = await ai_manager.async_chat(
        divide_reference_and_instruction_prompt.format(user_prompt=user_prompt)
    )

    print(f"user_instruction: {user_instruction}")

    keyword = await ai_manager.async_chat(
        find_keyword_prompt.format(user_instruction=user_instruction)
    )

    if keyword == NOT_TO_NEED_SEARCH_STRING:
        return user_prompt

    print(f"keyword: {keyword}")

    search = DuckDuckGoSearchRun()

    searched_result = await search.ainvoke(keyword)

    print(f"searched_result: {searched_result}")

    result = user_instruction + " ####reference\n " + searched_result
    print(f"result: {result}")
    return result
