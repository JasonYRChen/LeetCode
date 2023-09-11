class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        factors = set()
        for n in range(1, int(num**0.5) + 1):
            div, mod = divmod(num, n)
            if not mod:
                factors.add(n)
                factors.add(div)
        return sum(factors) == 2 * num
