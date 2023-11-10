from hash_table import *


if __name__ == "__main__":
    hashtable_example = create_hashtable()
    put(hashtable_example, 2, 2)
    put(hashtable_example, 10, 10)
    put(hashtable_example, 7, 7)
    put(hashtable_example, 13, 15)
    put(hashtable_example, 3, 9)
    print(remove(hashtable_example, 10))
    print(get(hashtable_example, 13))
    print(has_key(hashtable_example, 1))
    print(items(hashtable_example))
    hashtable_example = delete_hashtable(hashtable_example)
