class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num_map = {k:v for v, k in enumerate('0123456789')}
        carry = 0
        num = ''
        for n1, n2 in zip_longest(num1[::-1], num2[::-1], fillvalue='0'):
            digit = str(num_map[n1] + num_map[n2] + carry)
            carry = 1 if len(digit) == 2 else 0
            num = digit[-1] + num
        if carry:
            num = '1' + num
        return num
