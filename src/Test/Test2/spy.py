from functools import wraps
from time import time


def spy(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        parameters = {"args": args, "kwargs": kwargs}
        wrapper.calls.append((start_time, parameters, result))
        return result

    wrapper.calls = []
    return wrapper


def print_usage_statistic(function):
    if not hasattr(function, "calls"):
        raise ValueError(f"The function {function.__name__} is not decorated with @spy")

    for start_time, parameters, result in function.calls:
        yield {
            "function_name": function.__name__,
            "start_time": start_time,
            "parameters": parameters,
            "result": result,
        }


@spy
def foo(*args, **kwargs):
    print(args, kwargs)


def main():
    foo(5, key="1")
    foo("qwer", key="2")
    foo(15, key="3", message="home")
    foo(10)

    for call_info in print_usage_statistic(foo):
        str_parameters = " ".join(
            f"{k} = {v}" for k, v in call_info["parameters"].items()
        )
        print(
            f"Function {call_info['function_name']} was called at {call_info['start_time']} "
            f"with parameters: {str_parameters}."
        )


if __name__ == "__main__":
    main()
