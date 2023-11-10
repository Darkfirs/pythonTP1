from dataclasses import dataclass
from typing import *

Key = TypeVar("Key")
Value = TypeVar("Value")
def_capacity = 1024


@dataclass
class Node(Generic[Key, Value]):
    key: Key
    value: Value
    next: "Node" = None


@dataclass
class HashTable(Generic[Key, Value]):
    table: list[Optional["Node[Key, Value]"]]
    capacity: int = def_capacity
    size: int = 0
    hash_fn: Callable[[Any], Key] = hash

    def hash_func(self, key):
        return self.hash_fn(key) % self.capacity


def create_hashtable(capacity: int = def_capacity) -> HashTable:
    return HashTable([None] * capacity)


def put(hashtable: HashTable, key: Key, value: Value):
    if hashtable.table[hashtable.hash_func(key)] is None:
        hashtable.table[hashtable.hash_func(key)] = Node(key, value)
        hashtable.size += 1
    else:
        current = hashtable.table[hashtable.hash_func(key)]
        while current:
            if current.key == key:
                current.value = value
                return
            current = current.next
        new_node = Node(key, value)
        new_node.next = hashtable.table[hashtable.hash_func(key)]
        hashtable.table[hashtable.hash_func(key)] = new_node
        hashtable.size += 1


def items(hashtable: HashTable) -> list[tuple[Key, Value]]:
    res_pa = []
    num = 0
    while len(res_pa) != hashtable.size and num != hashtable.capacity:
        if hashtable.table[num] is not None:
            res_pa.append((hashtable.table[num].key, hashtable.table[num].value))
        num += 1
    return res_pa


def remove(hashtable: HashTable, key: Key) -> Value:
    if not has_key(hashtable, key):
        raise KeyError
    previous = None
    current = hashtable.table[hashtable.hash_func(key)]
    return_value = current.value
    while current:
        if current.key == key:
            if previous:
                previous.next = current.next
            else:
                hashtable.table[hashtable.hash_func(key)] = current.next
            hashtable.size -= 1
            return return_value
        previous = current
        current = current.next


def delete_hashtable(hashtable: HashTable):
    for num in range(hashtable.capacity):
        element_to_del = hashtable.table[num]

        def del_rec(element_to_delete):
            if element_to_delete is None:
                del element_to_delete
                return
            if element_to_delete.next is None:
                del element_to_delete.next
                del element_to_delete
                return
            del_rec(element_to_delete.next)

        del_rec(element_to_del)
    del hashtable


def get(hashtable: HashTable, key: Key) -> Value:
    if not has_key(hashtable, key):
        raise KeyError
    return hashtable.table[hashtable.hash_func(key)].value


def has_key(hashtable: HashTable, key: Key) -> bool:
    return hashtable.table[hashtable.hash_func(key)] is not None
