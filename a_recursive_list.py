class Node:
    value: any
    next: any

    def __init__(self, value, next):
        self.value = value
        self.next = next


class List:
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


def initialize() -> List:
    raise NotImplementedError("List.initialize() not defined")


def isEmpty(data: List) -> bool:
    raise NotImplementedError("List.isEmpty() not defined")


def addAtIndex(data: List, index: int, value: int) -> List:
    raise NotImplementedError("List.addAtIndex() not defined")


def removeAtIndex(data: List, index: int) -> tuple[Node, List]:
    def helper(v: Node, index, int, i:int):
        if i+1 == index:
            target: Node= v.next
            v.next = target.next
            
        return helper(v.next)


    raise NotImplementedError("List.removeAtIndex() not defined")


def addToFront(data: List, value: int) -> List:
    data.first = helper(data.first, value)
    if data.last is None:
        data.last = data.first
    return data

def helper(node: Node, value:int)-> Node:
    if node is None:
        return Node(value, None)
    else: 
        new_node = Node(value, node)
        return helper(new_node, node.value)
        

    
    
    
    raise NotImplementedError("List.addToFront() not defined")


def addToBack(data: List, value: int) -> List:
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

    raise NotImplementedError("List.addToBack() not defined")


def getElementAtIndex(data: List, index: int) -> Node:

    def helper(node: Node, index:int)->None:
        if node is None or index < 0:
            return None
        elif index == 0:
            return Node
        else:
            return helper(node.next, index -1)
    raise NotImplementedError("List.getElementAtIndex() not defined")


def clear(data: List) -> List:
    raise NotImplementedError("List.clear() not defined")
