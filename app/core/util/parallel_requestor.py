from app.core.util.ai_manager import AIManager


async def parallel_requestor(ai_manager: AIManager, user_prompt, loop_count):
    results = []
    for i in range(loop_count):
        results.append(await ai_manager.async_chat(user_prompt))
    return results
