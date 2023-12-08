from src.Practice.Practice_9.fsm import *
import pytest
from src.Practice.Practice_9.main_module import *
from string import digits



@pytest.fixture
def create_fs_d():
    digits_fsm_table = [
        {digits: 1, "+-": 5},
        {digits: 1, "E": 3, ".": 6},
        {digits: 2, "E": 3},
        {digits: 4, "+-": 7},
        {digits: 4},
        {digits: 1},
        {digits: 2},
        {digits: 4},
    ]
    return create_fs_machine(digits_fsm_table, 0, [1, 2, 4])


@pytest.fixture
def create_fs_abb():
    abb_fsm_table = [{"b": 0, "a": 1}, {"b": 2, "a": 1}, {"b": 3, "a": 1}, {"b": 0, "a": 1}]
    return create_fs_machine(abb_fsm_table, 0, [3])


@pytest.mark.parametrize(
    "string, expected",
    [
        ("", False),
        (" ", False),
        ("1111", False),
        ("abb", True),
        ("qwerty", False),
        ("bab", False),
        ("aabb", True),
        ("abba", False),
    ],
)
def test_validate_string_with_string_abb(string, expected, create_fs_abb):
    assert validate_string(create_fs_abb, string) == expected


@pytest.mark.parametrize(
    "string, expected",
    [
        (" ", False),
        ("", False),
        ("def", False),
        ("+def", False),
        ("3", True),
        (".11", False),
        ("1111", True),
        ("1.", False),
        ("13.12", True),
        ("1234.12E+7", True),
        ("115.23E+", False),
        ("163.23E", False),
    ],
)
def test_validate_digits(string, expected, create_fs_d):
    assert validate_string(create_fs_d, string) == expected


@pytest.mark.parametrize(
    "string_input, expected",
    [
        ("123abc", "This string match no language."),
        ("aabb", "This is abb-type language."),
        ("-1234.123E+12", "This is Digits language."),
        ("123.E", "This string match no language."),
    ],
)
def test_output_match(string_input, expected):
    assert speaker(string_input) == expected
