class Solution:
    def addDigits(self, num: int) -> int:
        if not num // 10:
            return num
        
        next_num = 0
        while num:
            num, r = divmod(num, 10)
            next_num += r
        return self.addDigits(next_num)
