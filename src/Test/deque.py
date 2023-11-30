from dataclasses import dataclass


@dataclass
class DequeNode:
    data: any
    next: "DequeNode" = None
    prev: "DequeNode" = None


@dataclass
class Deque:
    front: DequeNode = None
    rear: DequeNode = None
    size: int = 0


def create_deque():
    return Deque()


def push_front(deque, data):
    new_node = DequeNode(data)
    if deque.size == 0:
        deque.front = deque.rear = new_node
    else:
        new_node.next = deque.front
        deque.front.prev = new_node
        deque.front = new_node
    deque.size += 1


def push_back(deque, data):
    new_node = DequeNode(data)
    if deque.size == 0:
        deque.front = deque.rear = new_node
    else:
        new_node.prev = deque.rear
        deque.rear.next = new_node
        deque.rear = new_node
    deque.size += 1


def pop_front(deque):
    if deque.size == 0:
        raise IndexError("pop from an empty deque")
    data = deque.front.data
    if deque.size == 1:
        deque.front = deque.rear = None
    else:
        deque.front = deque.front.next
        deque.front.prev = None
    deque.size -= 1
    return data


def pop_back(deque):
    if deque.size == 0:
        raise IndexError("pop from an empty deque")
    data = deque.rear.data
    if deque.size == 1:
        deque.front = deque.rear = None
    else:
        deque.rear = deque.rear.prev
        deque.rear.next = None
    deque.size -= 1
    return data


def get_size(deque):
    return deque.size


def is_empty(deque):
    return deque.size == 0
