class Solution:
    def reverse(self, x: int) -> int:
        reverse = 0
        sign = 1 if x >= 0 else -1
        while x:
            x, mod = divmod(abs(x), 10)
            reverse = 10 * reverse + mod
        reverse *= sign
        return reverse if -2**31 <= reverse <= 2**31-1 else 0
