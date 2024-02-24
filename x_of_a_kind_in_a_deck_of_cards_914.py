class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        divisor = math.gcd(*Counter(deck).values())
        return True if divisor != 1 else False
