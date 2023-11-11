from dataclasses import dataclass


DEF_SIZE = 16

@dataclass
class HashTable:
    size: int
    table: list[list[tuple[str, object]]] = None

    def __post_init__(self):
        if self.table is None:
            self.table = [[] for _ in range(self.size)]


def hash_function(table_size: int, key: str) -> int:
    return hash(key) % table_size


def create_hash_table() -> HashTable:
    return HashTable(size=DEF_SIZE)


def delete_hash_table(hash_table: HashTable):
    del hash_table


def put(hash_table: HashTable, key: str, value: object):
    hash_value = hash_function(hash_table.size, key)
    bucket = hash_table.table[hash_value]
    for i, (existing_key, existing_value) in enumerate(bucket):
        if key == existing_key:
            bucket[i] = (key, value)
            break
    else:
        bucket.append((key, value))


def remove(hash_table: HashTable, key: str) -> object:
    hash_value = hash_function(hash_table.size, key)
    bucket = hash_table.table[hash_value]
    for i, (existing_key, existing_value) in enumerate(bucket):
        if key == existing_key:
            del bucket[i]
            return existing_value
    raise ValueError(f"Key '{key}' not found in the hash table")


def has_key(hash_table: HashTable, key: str) -> bool:
    hash_value = hash_function(hash_table.size, key)
    bucket = hash_table.table[hash_value]
    return any(existing_key == key for existing_key, _ in bucket)


def get(hash_table: HashTable, key: str) -> object:
    hash_value = hash_function(hash_table.size, key)
    bucket = hash_table.table[hash_value]
    for existing_key, existing_value in bucket:
        if key == existing_key:
            return existing_value
    raise ValueError(f"Key '{key}' not found in the hash table")


def items(hash_table: HashTable) -> list[tuple[str, object]]:
    result = []
    for bucket in hash_table.table:
        result.extend(bucket)
    return result
