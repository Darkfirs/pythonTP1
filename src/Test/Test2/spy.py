from functools import wraps
from datetime import datetime


def logger(log_file):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_time = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
            log_args = ", ".join(
                f"{k}={v}" for k, v in zip(func.__code__.co_varnames, args)
            )
            log_args += ", ".join(f"{k}={v}" for k, v in kwargs.items())

            try:
                result = func(*args, **kwargs)
                with open(log_file, "a") as file:
                    file.write(
                        f"{current_time} {func.__name__} {log_args} result={result}\n"
                    )
                return result
            except Exception as e:
                with open(log_file, "a") as file:
                    file.write(
                        f"{current_time} {func.__name__} {log_args} error={str(e)}\n"
                    )
                raise e

        return wrapper

    return decorator


@logger("my_log.txt")
def f(a, b):
    if a != 0:
        return f(a - 1, b - 1)
    return b


f(2, 1)
f(b=6, a=3)
