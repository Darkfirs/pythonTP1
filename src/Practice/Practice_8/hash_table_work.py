from hash_table import *


if __name__ == "__main__":
    hash_table = create_hash_table()
    put(hash_table, "name", "John")
    put(hash_table, "age", 25)
    print(get(hash_table, "name"))
    print(get(hash_table, "age"))
    put(hash_table, "age", 26)
    put(hash_table, '1', 1)
    put(hash_table, '2', 2)
    put(hash_table, '3', 3123)
    put(hash_table, '4', 4)
    print(get(hash_table, "age"))
    remove(hash_table, "name")
    print(has_key(hash_table, "age"))
    print(has_key(hash_table, "name"))
    print(has_key(hash_table, '3'))
    print(items(hash_table))
