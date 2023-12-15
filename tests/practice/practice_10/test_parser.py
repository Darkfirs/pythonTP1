import pytest
from src.Practice.Practice_10.main_module import *
from io import StringIO


@pytest.mark.parametrize(
    "file",
    [
        ("test1.txt"),
        ("test2.txt"),
        ("test3.txt"),
        ("test4.txt")
    ],
)
def test_main_scenario(monkeypatch, file):
    with open(file, "r") as file:
        input_str = file.readline()
        expected = file.readlines()
    monkeypatch.setattr("builtins.input", lambda _: input_str)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    output = fake_output.getvalue()
    assert output == "".join(expected)
