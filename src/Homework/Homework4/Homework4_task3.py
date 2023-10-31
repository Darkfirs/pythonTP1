from dataclasses import dataclass
from collections import namedtuple


QueueElement = namedtuple("QueueElement", ["value", "next"])

@dataclass
class Queue:
    size: int = 0
    head: QueueElement = None
    tail: QueueElement = None


def create_queue():
    return Queue()


def is_empty(queue: Queue):
    return queue.size == 0


def get_size(queue: Queue):
    return queue.size


def get_top(queue: Queue):
    if not is_empty(queue):
        return queue.tail.value


def to_pop(queue: Queue):
    if not is_empty(queue):
        queue.head = queue.head.next
        queue.size -= 1


def to_push(queue: Queue, value: any):
    new_element = QueueElement(value, None)
    if is_empty(queue):
        queue.head = new_element
    elif queue.size == 1:
        queue.tail = new_element
        queue.head = QueueElement(queue.head.value, queue.tail)
    else:
        queue.tail = QueueElement(value, new_element)
        queue.tail = new_element
    queue.size += 1
