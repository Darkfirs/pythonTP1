from fsm import *
from string import digits


def abb_type_language_validation(input_str: str) -> bool:
    abb_fsm_table = [
                {"b": 0, "a": 1},
                {"b": 2, "a": 1},
                {"b": 3, "a": 1},
                {"b": 0, "a": 1},
    ]
    fsm_abb = create_fs_machine(abb_fsm_table, start_state=0, accepted_states=[3])
    return validate_string(fsm_abb, input_str)


def add_digit_language_validation(input_str: str) -> bool:
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
    fsm_digits = create_fs_machine(
        digits_fsm_table, start_state=0, accepted_states=[1, 2, 4]
    )
    return validate_string(fsm_digits, input_str)


def speaker(enter: str):
    if abb_type_language_validation(enter):
        return "This is abb-type language"
    elif add_digit_language_validation(enter):
        return "This is Digits"
    else:
        return "The language wasn't found"


def main():
    enter = input("Input string: ")
    print(speaker(enter))


if __name__ == "__main__":
    main()
