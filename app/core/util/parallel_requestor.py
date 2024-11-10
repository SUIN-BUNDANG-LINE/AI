import asyncio
from app.core.util.ai_manager import AIManager
from app.core.util.allowed_other_manager import AllowedOtherManager

# 초당 최대 20번의 요청을 허용하는 세마포어 생성
semaphore = asyncio.Semaphore(20)


async def limited_request(ai_manager: AIManager, survey_creation_prompt):
    # 세마포어가 허용될 때까지 대기
    async with semaphore:
        # 요청을 보낸 후 1초 대기
        response = await ai_manager.async_chat(survey_creation_prompt)
        AllowedOtherManager.remove_last_choice_in_survey(parsed_survey)
        await asyncio.sleep(1)

        # 동기 파일 I/O로 결과를 기록
        with open("output_gpt_4o_mini.txt", "a") as f:
            f.write(f"{response}\n")
    return


async def parallel_requestor(ai_manager: AIManager, user_prompt, loop_count):
    tasks = [limited_request(ai_manager, user_prompt) for _ in range(loop_count)]
    results = await asyncio.gather(*tasks)
    return results
