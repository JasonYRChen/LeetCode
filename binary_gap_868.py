class Solution:
    def binaryGap(self, n: int) -> int:
        farthest = 0
        temp = 0
        while not n % 2:
            n //= 2

        while n:
            n, remainder = divmod(n, 2)
            if remainder:
                farthest = max(farthest, temp)
                temp = 0
            temp += 1
        return farthest
