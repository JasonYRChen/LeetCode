class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        distance = 0
        x ^= y
        while x:
            x, mod = divmod(x, 2)
            if mod:
                distance += 1
        return distance
