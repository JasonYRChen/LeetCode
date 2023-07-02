class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n < 0:
            return 0
        
        total, multiple = 1, 9
        for i in range(n):
            total *= multiple
            if i != 0:
                multiple -= 1
        return total + self.countNumbersWithUniqueDigits(n - 1)
