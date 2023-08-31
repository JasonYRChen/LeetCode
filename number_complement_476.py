class Solution:
    def findComplement(self, num: int) -> int:
        n = num
        power = 0
        while n:
            n >>= 1
            power += 1
        return num ^ (2 ** power - 1)
