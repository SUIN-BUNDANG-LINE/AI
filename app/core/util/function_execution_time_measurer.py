import time


class FunctionExecutionTimeMeasurer:
    @staticmethod
    def run_function(business_function, *args, **kwargs):
        start_time = time.time()
        result = business_function(*args, **kwargs)
        end_time = time.time()
        print(f"{business_function.__name__} 호출 : {end_time - start_time:.4f} seconds")
        return result
