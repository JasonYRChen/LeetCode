class DoubleLinkedList:
    __slots__ = 'val', 'prev', 'follow'

    def __init__(self, val=None, prev=None, follow=None):
        self.val = val
        self.prev = prev
        self.follow = follow

    @staticmethod
    def reconnect(prev_node, next_node):
        prev_node.follow, next_node.prev = next_node, prev_node


class MinStack:
    def __init__(self):
        self.stack = []
        self.head = DoubleLinkedList()
        self.tail = DoubleLinkedList(float('inf'))
        DoubleLinkedList.reconnect(self.head, self.tail)

    def push(self, val: int) -> None:
        new_node = DoubleLinkedList(val)
        self.stack.append(new_node)
        if val < self.head.follow.val:
            DoubleLinkedList.reconnect(new_node, self.head.follow)
            DoubleLinkedList.reconnect(self.head, new_node)
        else:
            DoubleLinkedList.reconnect(self.tail.prev, new_node)
            DoubleLinkedList.reconnect(new_node, self.tail)

    def pop(self) -> None:
        node = self.stack.pop()
        DoubleLinkedList.reconnect(node.prev, node.follow)

    def top(self) -> int:
        return self.stack[-1].val

    def getMin(self) -> int:
        return self.head.follow.val


if __name__ == '__main__':
    m = MinStack()
    m.push(-2)
    m.push(0)
    m.push(-3)
    print(m)

