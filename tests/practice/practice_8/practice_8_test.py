import pytest
from src.Practice.Practice_8.hash_table import *


def dummy_hash_table(elements: tuple):
    hash_table = create_hash_table()
    for i in elements:
        put(hash_table, i[0], i[1])
    return hash_table


def test_create_hash_table():
    has_table = create_hash_table()
    assert isinstance(has_table, HashTable)


def test_remove():
    hash_table = create_hash_table()
    key = "test_key"
    value = "test_value"
    put(hash_table, key, value)
    removed_value = remove(hash_table, key)
    assert removed_value == value
    with pytest.raises(ValueError, match=f"Key '{key}' not found in the hash table"):
        remove(hash_table, key)


@pytest.mark.parametrize(
    "elements,key",
    [
        ((("may 1", 1), ("may 2", 2), ("may 3", 3), ("may 4", 4)), "may 123"),
        ((("may 1", 1), ("may 2", 2), ("may 3", 3), ("may 4", 4)), "may 23"),
        ((("may 1", 1), ("may 2", 2), ("may 3", 3), ("may 4", 4)), "may 5"),
    ],
)
def test_error_remove(elements, key):
    hash_table = dummy_hash_table(elements)
    with pytest.raises(ValueError):
        remove(hash_table, key)


@pytest.mark.parametrize(
    "elements,key,expected",
    [
        ((("may 1", 1), ("may 2", 2), ("may 3", 3), ("may 4", 4)), "may 4", 4),
        ((("may 1", 1), ("may 2", 2), ("may 3", 3), ("may 4", 4)), "may 3", 3),
        ((("may 1", 1), ("may 2", 2), ("may 3", 3), ("may 4", 4)), "may 1", 1),
    ],
)
def test_get(elements, key, expected):
    hash_table = dummy_hash_table(elements)
    assert get(hash_table, key) == expected


@pytest.mark.parametrize(
    "elements,key",
    [
        ((("may 1", 1), ("may 2", 2), ("may 3", 3), ("may 4", 4)), "may 123"),
        ((("may 1", 1), ("may 2", 2), ("may 3", 3), ("may 4", 4)), "may 23"),
        ((("may 1", 1), ("may 2", 2), ("may 3", 3), ("may 4", 4)), "may 5"),
    ],
)
def test_error_get(elements, key):
    hash_table = dummy_hash_table(elements)
    with pytest.raises(ValueError):
        get(hash_table, key)


@pytest.mark.parametrize(
    "elements,key,expected",
    [
        ((("may 1", 1), ("may 2", 2), ("may 3", 3), ("may 4", 4)), "may 4", True),
        ((("may 1", 1), ("may 2", 2), ("may 3", 3), ("may 4", 4)), "may 3", True),
        ((("may 1", 1), ("may 2", 2), ("may 3", 3), ("may 4", 4)), "may 11", False),
    ],
)
def test_has_key(elements, key, expected):
    hash_table = dummy_hash_table(elements)
    assert has_key(hash_table, key) == expected


def test_items():
    hash_table = create_hash_table()
    put(hash_table, "key1", "value1")
    put(hash_table, "key3", "value3")
    put(hash_table, "key2", "value2")
    result = items(hash_table)
    expected_result = [("key1", "value1"), ("key2", "value2"), ("key3", "value3")]
    assert result == expected_result


@pytest.mark.parametrize("key, value", [("test_key", "test_value"), ("another_key", 42)])
def test_put_and_get(key, value):
    hash_table = create_hash_table()
    put(hash_table, key, value)
    retrieved_value = get(hash_table, key)
    assert retrieved_value == value
