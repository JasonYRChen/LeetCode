from collections import deque


class MyQueue:

    def __init__(self):
        self.data = deque()

    def push(self, x: int) -> None:
        self.data.append(x)

    def pop(self) -> int:
        return self.data.popleft() if self.data else []

    def peek(self) -> int:
        return self.data[0] if self.data else []

    def empty(self) -> bool:
        return False if self.data else True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
