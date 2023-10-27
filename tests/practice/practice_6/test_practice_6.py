from Practice.Practice_6.practice_6_Abramov import *
from io import StringIO
import pytest


@pytest.mark.parametrize("a,b,c", [(100, 5, 2.9), (10, 1, 2), (-10, 20, -40)])
def test_raise_exception_quadratic_equation(a, b, c):
    with pytest.raises(ArithmeticError):
        solution_quadratic(a, b, c)


@pytest.mark.parametrize(
    "a,b,c,expected",
    [
        (1, 10, 9, (-9, -1)),
        (2, -1, -15, (3, -2.5)),
        (-1, 0, 1, (-1, 1)),
        (1.5, 12.2, 4, (-7.791060726256911, -0.3422726070764212)),
        (8.5, 6, 0, (0.0, -0.7058823529411765)),
    ],
)
def test_quadratic_two_roots(a, b, c, expected):
    actual = solution_quadratic(a, b, c)
    assert len(actual) == 2 and actual[0] in expected and actual[1] in expected


@pytest.mark.parametrize(
    "a,b,c,expected",
    [
        (8.86, 0, 0, (0.0,)),
        (-20, 20, -5, (0.5,)),
        (1, 4, 4, (-2,)),
        (5, 7, 2.45, (-0.7,)),
    ],
)
def test_quadratic_one_roots(a, b, c, expected):
    actual = solution_quadratic(a, b, c)
    assert len(actual) == 1 and actual == expected


@pytest.mark.parametrize(
    "b,c,expected", [(50, -100, (2,)), (10.5, 105, (-10,)), (-4, -62, (-15.5,))]
)
def test_linear_equation(b, c, expected):
    actual = solution_linear(b, c)
    assert actual == expected


@pytest.mark.parametrize("c", [1, 0.5, -99.9, 0])
def test_raise_exception_const(c):
    with pytest.raises(ArithmeticError):
        solve_constant_equation(c)


@pytest.mark.parametrize(
    "coefficient,expected",
    [
        ("2.1", True),
        ("-1.09", True),
        ("5", True),
        ("f", False),
        (",", False),
        ("...", False),
        ("+", False),
        (";", False),
        (":", False),
    ],
)
def test_float_number(coefficient, expected):
    assert float_numbers(coefficient) == expected


@pytest.mark.parametrize(
    "coefficients, expected",
    [
        ("0 -99.9 45.56", (0.0, -99.9, 45.56)),
        ("123 0.9 1", (123.0, 0.9, 1.0)),
        ("1.1 2.3 456.9", (1.1, 2.3, 456.9)),
    ],
)
def test_checking_arguments(coefficients, expected):
    actual = checking_arguments(coefficients)
    assert actual == expected


@pytest.mark.parametrize("coefficients", ["5 5", "5 h g", "h g", "2..5 4 5", "2,5 5 0"])
def test_raise_exception_parse_user_input(coefficients):
    with pytest.raises(ValueError):
        checking_arguments(coefficients)


@pytest.mark.parametrize(
    "a,b,c,expected",
    [
        (2, -1, -15, (-2.5, 3)),
        (-1, 0, 1, (-1.0, 1.0)),
        (1, 8, 16, (-4.0,)),
        (0, -100, 200, (2,)),
    ],
)
def test_solve_equations(a, b, c, expected):
    assert select_formula(a, b, c) == expected

@pytest.mark.parametrize(
    "user_input,expected",
    [
        ("2 -1 -15", "Solution: -2.5 3.0\n"),
        ("1 8 16", "Solution: -4.0\n"),
        ("1 2 3", "Discriminant must be non-negative\n"),
        ("1 2 1", "Solution: -1.0\n"),
        ("0 0 0", "Infinitely many solutions\n"),
        ("0 0 5", "No solutions\n"),
    ],
)
def test_main_scenario(monkeypatch, user_input, expected):
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    fake_output = StringIO()
    main()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    output = fake_output.getvalue()
    assert output == expected
