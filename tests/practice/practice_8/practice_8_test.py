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
        ((("key 1", 1), ("key 2", 2), ("key 3", 3), ("key 4", 4)), "key 1234"),
        ((("key 1", 1), ("key 2", 2), ("key 3", 3), ("key 4", 4)), "key 5678"),
        ((("key 1", 1), ("key 2", 2), ("key 3", 3), ("key 4", 4)), "key 91011"),
    ],
)
def test_error_remove(elements, key):
    hash_table = dummy_hash_table(elements)
    with pytest.raises(ValueError):
        remove(hash_table, key)


@pytest.mark.parametrize(
    "elements,key,expected",
    [
        ((("key 1", 1), ("key 2", 2), ("key 3", 3), ("key 4", 4)), "key 1", 1),
        ((("key 1", 1), ("key 2", 2), ("key 3", 3), ("key 4", 4)), "key 2", 2),
        ((("key 1", 1), ("key 2", 2), ("key 3", 3), ("key 4", 4)), "key 3", 3),
    ],
)
def test_get(elements, key, expected):
    hash_table = dummy_hash_table(elements)
    assert get(hash_table, key) == expected


def test_items():
    hash_table = create_hash_table()
    put(hash_table, "key1", "value1")
    put(hash_table, "key3", "value3")
    put(hash_table, "key2", "value2")
    result = items(hash_table)
    expected_result = [("key1", "value1"), ("key2", "value2"), ("key3", "value3")]
    assert result == expected_result


@pytest.mark.parametrize(
    "elements,key,expected",
    [
        ((("key 1", 1), ("key 2", 2), ("key 3", 3), ("key 4", 4)), "key 1", True),
        ((("key 1", 1), ("key 2", 2), ("key 3", 3), ("key 4", 4)), "key 11", False),
        ((("key 1", 1), ("key 2", 2), ("key 3", 3), ("key 4", 4)), "key 2", True),
    ],
)
def test_has_key(elements, key, expected):
    hash_table = dummy_hash_table(elements)
    assert has_key(hash_table, key) == expected


@pytest.mark.parametrize(
    "key, value", [("test_key", "test_value"), ("another_key", 42)]
)
def test_put_and_get(key, value):
    hash_table = create_hash_table()
    put(hash_table, key, value)
    retrieved_value = get(hash_table, key)
    assert retrieved_value == value


@pytest.mark.parametrize(
    "elements,key",
    [
        ((("key 1", 1), ("key 2", 2), ("key 3", 3), ("key 4", 4)), "key 1000"),
        ((("key 1", 1), ("key 2", 2), ("key 3", 3), ("key 4", 4)), "key 7"),
        ((("key 1", 1), ("key 2", 2), ("key 3", 3), ("key 4", 4)), "key 1234"),
    ],
)
def test_error_get(elements, key):
    hash_table = dummy_hash_table(elements)
    with pytest.raises(ValueError):
        get(hash_table, key)
