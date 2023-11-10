from src.Practice.Practice_8.hash_table import *
import pytest


def test_create_hashtable():
    test_hashtable = create_hashtable()
    assert (
        test_hashtable.capacity == 1024
        and len(test_hashtable.table) == 1024
        and test_hashtable.size == 0)


def dummy_hashtable(elements):
    hashtable = create_hashtable()
    for i in elements:
        put(hashtable, i[0], i[1])
    return hashtable


def test_delete_hashtable():
    test_hashtable = create_hashtable()
    test_hashtable = delete_hashtable(test_hashtable)
    assert test_hashtable is None


@pytest.mark.parametrize(
    "elements, put_element, expected",
    (
        (((7, 12), (2, 5), (3, 1)), (18, 15), [(2, 5), (3, 1), (7, 12), (18, 15)]),
        (
            ((1, 1), (2, 2), (3, 3)),
            ("Notnone", None),
            [(1, 1), (2, 2), (3, 3), ("Notnone", None)],
        ),
    ),
)
def test_put(elements, put_element, expected):
    test_hashtable = dummy_hashtable(elements)
    put(test_hashtable, *put_element)
    assert items(test_hashtable) == expected


@pytest.mark.parametrize(
    "elements, find_key, expected",
    (
        (((1, 1), (2, 2), (3, 3), ("Notnone", None)), "Notnone", True),
        (((1, 1), (2, 2), (3, 3), (15, 15)), 2, True),
        (((20, 20), (30, 30)), 15, False),
    ),
)
def test_has_key(elements, find_key, expected):
    test_hashtable = dummy_hashtable(elements)
    assert has_key(test_hashtable, find_key) == expected


@pytest.mark.parametrize(
    "elements, get_key, expected",
    (
        (((1, 1), (2, 2), (3, 3), ("Notnone", None)), "Notnone", None),
        (((1, 1), (2, 2), (3, 3), (5, 5)), 2, 2),
        (((20, 20), (30, 30), (19, "qwer")), 19, "qwer"),
    ),
)
def test_get(elements, get_key, expected):
    test_hashtable = dummy_hashtable(elements)
    assert get(test_hashtable, get_key) == expected

def test_remove_error():
    test_hashtable = create_hashtable()
    with pytest.raises(KeyError):
        assert remove(test_hashtable, 4) == KeyError


def test_get_error():
    test_hashtable = create_hashtable()
    with pytest.raises(KeyError):
        assert get(test_hashtable, 10) == KeyError

@pytest.mark.parametrize(
    "elements, expected",
    (
        (
            ((1, 1), (2, 2), (3, 3), ("Notnone", None)),
            [(1, 1), (2, 2), (3, 3), ("Notnone", None)],
        ),
        (((1, 1), (7, 7), (3, 3), (9, 9)), [(1, 1), (3, 3), (7, 7), (9, 9)]),
        (((25, 25), (50, 50)), [(25, 25), (50, 50)]),
    ),
)
def test_items(elements, expected):
    test_hashtable = dummy_hashtable(elements)
    assert items(test_hashtable) == expected