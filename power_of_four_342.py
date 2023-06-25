class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n > 1:
            n, remain = divmod(n, 4)
            if remain:
                return False
        return True if n == 1 else False
