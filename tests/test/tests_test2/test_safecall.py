from src.Test.Test2.safecall import safe_call
import pytest
import warnings


@safe_call
def ex_funct_1(a, b):
    return a + b


@safe_call
def ex_funct_2(a, b):
    return a / b


@pytest.mark.parametrize(
    "num_1, num_2, expected",
    [(5, 10, 15), (20, 10, 30), (1, 2, 3)],
)
def test_work_functions_correct(num_1, num_2, expected):
    assert ex_funct_1(num_1, num_2) == expected


@pytest.mark.parametrize(
    "num_1, num_2, expected",
    [(2, 0, None)],
)
def test_work_functions_error(num_1, num_2, expected, capsys):
    with capsys.disabled():
        with warnings.catch_warnings(record=True) as w:
            result = ex_funct_2(num_1, num_2)
            assert result == expected

            assert len(w) == 1
            warning = w[0].message
            assert str(warning) == (
                f"Warning:\n"
                f"Function: ex_funct_2\n"
                f"Type of Exception: ZeroDivisionError\n"
                f"Message: division by zero\n"
                f"In line return a / b\n"
            )


@pytest.mark.parametrize(
    "num_1, num_2, expected",
    [(2, "b", None)],
)
def test_work_functions_error_strtyps(num_1, num_2, expected, capsys):
    with capsys.disabled():
        with warnings.catch_warnings(record=True) as w:
            result = ex_funct_2(num_1, num_2)
            assert result == expected

            assert len(w) == 1
            warning = w[0].message
            assert str(warning) == (
                f"Warning:\n"
                f"Function: ex_funct_2\n"
                f"Type of Exception: TypeError\n"
                f"Message: unsupported operand type(s) for /: 'int' and 'str'\n"
                f"In line return a / b\n"
            )
