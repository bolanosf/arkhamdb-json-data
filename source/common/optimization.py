import time


def runtime_function(func_name, func, args):
    start_time = time.time()
    return_obj = func(**args)
    print(f"Time for {func_name} to run: {time.time() - start_time}")
    return return_obj
