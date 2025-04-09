import json
import os

import requests
from dotenv import load_dotenv

from app.core.prompt.find_keyword_prompt import find_keyword_prompt
from app.core.util.function_execution_time_measurer import FunctionExecutionTimeMeasurer

load_dotenv()
serperAPIKey = os.getenv("SERPER_API_KEY")


def get_searched_result_by(keyword):
    if keyword is None:
        return ""
    if keyword == "":
        return ""

    searched_url = get_searched_url(keyword)
    print(f"searched_url: {searched_url}")
    if searched_url == "":
        return ""

    searched_result = get_searched_result(searched_url)
    print(f"searched_result: {searched_result}")
    if len(searched_result) < 100:
        searched_result += get_searched_result(searched_url)
        print(f"searched_result: {searched_result}")

    return searched_result


def get_searched_url(keyword):
    payload = json.dumps({"q": keyword, "gl": "kr", "hl": "ko"})
    headers = {
        "X-API-KEY": serperAPIKey,
        "Content-Type": "application/json",
    }

    searched_link = ""
    response = requests.request("POST", "https://google.serper.dev/search", headers=headers, data=payload)

    if response.status_code != 200:
        return ""

    for i, result in enumerate(response.json()["organic"]):
        link = result["link"]
        if link.startswith("https://www.youtube.com/"):
            continue
        else:
            searched_link = link
            break

    if searched_link == "":
        return ""

    return searched_link


def get_searched_result(searched_url):
    payload = json.dumps({
        "url": searched_url
    })
    headers = {
        'X-API-KEY': serperAPIKey,
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", "https://scrape.serper.dev", headers=headers, data=payload)

    if response.status_code != 200:
        return ""

    searched_result = ""
    try:
        response_json = response.json()
        searched_result = response_json["text"]
    except:
        pass

    return searched_result


def get_user_prompt_with_searched_result(ai_manager, user_prompt):
    searched_result = FunctionExecutionTimeMeasurer.run_function(
        "유저 프롬프트 키워드 추출/검색/개선 태스크",
        get_searched_result_by,
        ai_manager.chat(find_keyword_prompt.format(user_prompt=user_prompt))
    )
    if searched_result == "":
        return user_prompt
    return user_prompt + "reference) " + searched_result
