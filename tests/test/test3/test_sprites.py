from src.Test.Test3.sprites import *
import pytest
from io import StringIO


@pytest.mark.parametrize(
    "num,expected", [(4, True), (-5, False), ("b", False), (15, True), (0, False)]
)
def test_check_number(num, expected):
    assert check_number(num) == expected


@pytest.mark.parametrize("size", [4, 5, 8, 10])
def test_draw_sprite(size, capsys):
    sprite = generate_symmetric_sprite(size)
    draw_sprite(sprite)

    captured = capsys.readouterr()
    for row in sprite:
        assert "".join(row) in captured.out


def is_symmetric(sprite):
    return all(row == row[::-1] for row in sprite)


@pytest.mark.parametrize("size", [4, 5, 8, 10])
def test_generate_symmetric_sprite(size):
    sprite = generate_symmetric_sprite(size)

    assert len(sprite) == size // 2 + size % 2
    assert all(len(row) == 2 * size for row in sprite)

    assert is_symmetric(sprite)

    if size % 2 == 1:
        assert is_symmetric([sprite[size // 2]])


@pytest.mark.parametrize(
    "user_input,expected",
    [
        (-5, "Число должно быть больше 0\n"),
        ("b", "Вы должны ввести число\n"),
        (-5, "Число должно быть больше 0\n"),
    ],
)
def test_main_scenario(monkeypatch, user_input, expected):
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    fake_output = StringIO()
    main(user_input)
    monkeypatch.setattr("sys.stdout", fake_output)
    main(user_input)
    output = fake_output.getvalue()
    assert output == expected
