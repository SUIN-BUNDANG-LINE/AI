from langchain_community.tools import DuckDuckGoSearchRun
from app.core.util.ai_manager import AIManager
from app.core.prompt.improve_user_prompt_with_searched_result_prompt import (
    improve_user_prompt_with_searched_result_prompt,
)


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

    print(f"keyword: {keyword}")

    if keyword == NOT_TO_NEED_SEARCH_STRING:
        return user_prompt

    search = DuckDuckGoSearchRun()

    searched_result = search.invoke(keyword)

    print(f"searched_result: {searched_result}")

    result = user_prompt + " " + user_instruction + "\nreference)\n" + searched_result
    print(f"result: {result}")
    return result


async def async_chat_improve_user_prompt_with_search(
    ai_manager: AIManager, user_prompt, keyword
):
    if keyword == "":
        return

    if keyword == NOT_TO_NEED_SEARCH_STRING:
        return user_prompt

    print(f"keyword: {keyword}")

    searched_result = await DuckDuckGoSearchRun().ainvoke(keyword)
    print(f"searched_result: {searched_result}")
    #
    # improved_user_prompt = await ai_manager.async_chat(
    #     improve_user_prompt_with_searched_result_prompt.format(
    #         user_prompt=user_prompt, search_result=searched_result
    #     )
    # )

    improved_user_prompt = user_prompt + "\n#### context\n" + searched_result
    print(f"improved user prompt: {improved_user_prompt}")
    return improved_user_prompt
