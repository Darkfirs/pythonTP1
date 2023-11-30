import pytest
from src.Test.Test2.fibonacci import *
from io import StringIO


@pytest.mark.parametrize(
    "n, expected", [(0, 0), (1, 1), (10, 55), (90, 2880067194370816120)]
)
def test_fibonacci(n, expected):
    assert fibonacci(n) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        ("12", True),
        ("001", True),
        ("qwer", False),
        ("100", False),
        ("-1", False),
        ("10.5", False),
        (":", False),
        ("-0", False),
        ("55", True),
    ],
)
def test_check_input(n, expected):
    assert check_enter(n) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        ("0", "0\n"),
        ("12", "144\n"),
        ("90", "2880067194370816120\n"),
        ("qwer", "You must enter integer number\n"),
        ("125", "You must enter number between 0 and 90\n"),
        ("15.5", "You must enter integer number\n"),
    ],
)
def test_main(monkeypatch, n, expected):
    monkeypatch.setattr("builtins.input", lambda _: n)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    output = fake_output.getvalue()
    assert output == expected
