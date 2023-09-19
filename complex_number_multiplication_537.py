class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        r1, i1 = num1.split('+')
        r2, i2 = num2.split('+')
        r1, i1, r2, i2 = int(r1), int(i1[:-1]), int(r2), int(i2[:-1])
        real = r1 * r2 - i1 * i2
        imag = r1 * i2 + r2 * i1
        return f'{real}+{imag}i'
