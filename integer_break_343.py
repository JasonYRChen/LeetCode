class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 7:
            return (n // 2) * (n - n // 2)
        return 3 * self.integerBreak(n - 3)
