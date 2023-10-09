from dataclasses import dataclass
from collections import namedtuple


StackElement = namedtuple("StackElement",["value","next"])


@dataclass
class Stack:
    size : int = 0
    head : StackElement = None


def size(stack : Stack):
    return stack.size


def empty(stack : Stack):
    return stack.size == 0


def top(stack : Stack):
    if not empty(stack):
        return stack.head.value


def pop(stack: Stack) -> None:
    if not empty(stack):
        stack.size -= 1
        stack.head = stack.head.next


def push(stack : Stack,value:any):
    stack.size += 1
    new = StackElement(value,stack.head)
    stack.head = new


if __name__ == "__main__":
    stack1 = Stack()
    for i in range(15):
        push(stack1,i)
    print(empty(stack1))
    print(top(stack1))
    pop(stack1)
    print(top(stack1))


