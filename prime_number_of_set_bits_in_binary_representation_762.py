class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0
        prime = {2, 3, 5, 7, 11, 13, 17, 19}
        for num in range(left, right + 1):
            count += num.bit_count() in prime
        return count
