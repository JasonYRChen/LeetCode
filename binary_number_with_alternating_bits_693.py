class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n = n + n // 2
        while n:
            n, r = divmod(n, 2)
            if not r:
                return False
        return True
