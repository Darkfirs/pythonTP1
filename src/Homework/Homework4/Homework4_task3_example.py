from Homework4_task3 import *


if __name__ == '__main__':
    queue = create_queue()
    print(f"size:",get_size(queue))
    print("add 14 numbers")
    for i in range(1,15):
        to_push(queue, i)
    print(is_empty(queue))
    print(f"new size:",get_size(queue))
    print(f"top:",get_top(queue))
    print(last(queue))