class Solution:
    def convertToBase7(self, num: int) -> str:
        if not num:
            return '0'
            
        string = ''
        sign = ''
        if num < 0:
            sign = '-'
            num = abs(num)

        while num:
            num, mod = divmod(num, 7)
            string = str(mod) + string
        return sign + string
