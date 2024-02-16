class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.array = encoding
        self.index = 0

    def next(self, n: int) -> int:
        while n:
            if self.index == len(self.array):
                return -1
            if not self.array[self.index]:
                self.index += 2
            else:
                subtraction = min(n, self.array[self.index])
                n -= subtraction
                self.array[self.index] -= subtraction
        return self.array[self.index + 1]


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)
