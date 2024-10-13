import time


class FunctionExecutionTimeMeasurer:
    @staticmethod
    def run_function(task_name, business_function, *args, **kwargs):
        start_time = time.time()
        result = business_function(*args, **kwargs)
        end_time = time.time()
        print(f"{task_name} 소요 시간 : {end_time - start_time:.4f} seconds")
        return result

    @staticmethod
    async def run_async_function(task_name, business_function, *args, **kwargs):
        start_time = time.time()
        result = await business_function(*args, **kwargs)
        end_time = time.time()
        print(f"{task_name} 소요 시간 : {end_time - start_time:.4f} seconds")
        return result
