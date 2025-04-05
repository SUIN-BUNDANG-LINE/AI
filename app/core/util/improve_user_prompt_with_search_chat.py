import json
import os
import re

import requests
from dotenv import load_dotenv

from app.core.prompt.find_keyword_prompt import find_keyword_prompt
from app.core.util.ai_manager import AIManager

load_dotenv()

serperAPIKey = os.getenv("SERPER_API_KEY")


def remove_html(sentence):
    sentence = re.sub(r"<script>.*?</script>", "", sentence, flags=re.DOTALL)
    sentence = re.sub("(<([^>]+)>)", "", sentence)
    sentence = re.sub("&nbsp;", "", sentence)
    return sentence


def get_searched_result(keyword):
    payload = json.dumps({"q": keyword, "gl": "kr", "hl": "ko"})
    headers = {
        "X-API-KEY": serperAPIKey,
        "Content-Type": "application/json",
    }

    searched_link = ""
    response = requests.request(
        "POST", "https://google.serper.dev/search", headers=headers, data=payload
    )
    for i, result in enumerate(response.json()["organic"]):
        link = result["link"]
        if link.startswith("https://www.youtube.com/"):
            continue
        else:
            searched_link = link
            break
    if searched_link == "":
        return ""

    response = requests.get(searched_link)
    if response.status_code == 200:
        html = response.text
        return remove_html(html)
    else:
        return ""


def chat_improve_user_prompt_with_search(ai_manager: AIManager, user_prompt):
    if user_prompt == "":
        return

    keyword = ai_manager.chat(find_keyword_prompt.format(user_prompt=user_prompt))

    print(f"keyword: {keyword}")
    searched_result = get_searched_result(keyword)
    print(f"searched_result: {searched_result}")
    return user_prompt + "\nreference)\n" + searched_result
