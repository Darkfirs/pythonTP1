from dataclasses import dataclass
from collections import namedtuple
from typing import *


QueueElement = namedtuple("QueueElement", ["value", "next"])

@dataclass
class Queue:
    size: int = 0
    head: Optional[QueueElement] = None
    tail: QueueElement = None


def create_queue():
    return Queue()


def is_empty(queue: Queue):
    return queue.size == 0


def last(queue):
    if not is_empty(queue):
        return queue.tail.value
    return None


def get_size(queue: Queue):
    return queue.size


def get_top(queue: Queue):
    if not is_empty(queue):
        return queue.tail.value
    return None


def pop(queue: Queue):
    if not is_empty(queue):
        queue.head = queue.head.next
        queue.size -= 1


def to_push(queue: Queue, value: any):
    new_element = QueueElement(value, None)
    if is_empty(queue):
        queue.head = new_element
    else:
        queue.tail = QueueElement(value, new_element)
        queue.tail = new_element
    queue.size += 1
