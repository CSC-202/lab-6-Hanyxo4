class Node:
    value: any
    next: any

    def __init__(self, value, next):
        self.value = value
        self.next = next


class Stack:
    first: Node
    last: Node

    def __init__(self):
        self.first = None
        self.last = None

    def __len__(self):
        n: int = 0
        current = self.first
        while current != None:
            n += 1
            current = current.next
        return n

    def toPythonList(self):
        result: list = []
        current = self.first
        while current != None:
            result.append(current.value)
            current = current.next
        return result


def initialize() -> Stack:
    return Stack()
    raise NotImplementedError("Stack.initialize() not defined")


def isEmpty(data: Stack) -> bool:
    if data.first is None:
        return True
    else:
        return False
    raise NotImplementedError("Stack.isEmpty() not defined")


def push(data: Stack, value: int) -> Stack:
    data.first = helper(data.first, value)
    if data.last is None:
        data.last = data.first
    return data
def helper(node:Node, value:int)-> Node:
    if node is None:
        return Node(value, None)
    else:

        node.next = helper(node.next, value)
        return node
    raise NotImplementedError("Stack.push() not defined")


def pop(data: Stack) -> tuple[Node, Stack]:
    if data.first is None:
        return None, data
    else:
        pop = data.first
        data.first = pop.next
        if data.first is None:
            data.last = None
        return pop, data
    raise NotImplementedError("Stack.pop() not defined")


def peek(data: Stack) -> Node:
    if data.first is None:
        return None
    else:
        return data.first
    raise NotImplementedError("Stack.peek() not defined")


def clear(data: Stack) -> Stack:
    data.first = None
    data.last = None

    return data
    raise NotImplementedError("Stack.clear() not defined")
