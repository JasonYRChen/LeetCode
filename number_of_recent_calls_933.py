class RecentCounter:

    def __init__(self):
        self.array = []

    def ping(self, t: int) -> int:
        self.array.append(t)
        left, right = 0, len(self.array)
        target = t - 3000
        while left < right:
            mid = (left + right) // 2
            if self.array[mid] < target:
                left = mid + 1
            else:
                right = mid
        self.array = self.array[left:]
        return len(self.array)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
