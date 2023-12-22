import traceback
import warnings
from functools import wraps


def safe_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            error_info = {
                "function": func.__name__,
                "exception_type": type(e).__name__,
                "exception_message": str(e),
                "traceback": traceback.format_exc(),
            }
            warning_message = (
                f"Warning:\n"
                f"Function: {error_info['function']}\n"
                f"Type of Exception: {error_info['exception_type']}\n"
                f"Message: {error_info['exception_message']}\n"
                f"In line {error_info['traceback'].splitlines()[-2].lstrip('  ')}\n"
            )
            warnings.warn(warning_message, category=UserWarning)
            return None

    return wrapper


@safe_call
def example_function(dividend, divisor):
    result = dividend / divisor
    return result


result = example_function(10, 2)
print("Result:", result)

result = example_function(10, "b")
print("Result:", result)
