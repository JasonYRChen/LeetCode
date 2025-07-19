class Solution:
    def bitwiseComplement(self, n: int) -> int:
        ans = 0 if n else 1
        power = 0
        while n:
            n, remainder = divmod(n, 2)
            if not remainder:
                ans += 2 ** power
            power += 1
        return ans
