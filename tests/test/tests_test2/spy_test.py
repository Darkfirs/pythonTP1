from src.Test.Test2.spy import *


@spy
def foo(a, b):
    return a, b


@spy
def goo():
    return True


def test_print_usage_statistic():
    value = [i for i in print_usage_statistic(foo)]
    assert "".join(value) == ""


def test_print_usage():
    for _ in range(41):
        goo()
    result = list(print_usage_statistic(goo))
    assert len(result) == 41
