class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        total = 1
        stack = self.stack
        while stack and price >= stack[-1][0]:
            total += stack.pop()[1]
        stack.append((price, total))
        return total


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
