from deque import *

if __name__ == "__main__":
    deque = create_deque()
    push_front(deque, 1)
    push_back(deque, 2)
    push_front(deque, 3)
    print("size:", get_size(deque))
    front_element = pop_front(deque)
    rear_element = pop_back(deque)
    print("front element:", front_element)
    print("rear element:", rear_element)
    print("is empty:", is_empty(deque))