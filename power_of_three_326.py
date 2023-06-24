class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n > 1:
            n, remain = divmod(n, 3)
            if remain:
                return False
        return True if n > 0 else False
