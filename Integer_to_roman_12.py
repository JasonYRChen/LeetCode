class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = [['I', 'V', 'X'], ['X', 'L', 'C'], ['C', 'D', 'M'], ['M']]
        roman = ''
        for n, symbol in zip(str(num)[::-1], symbols):
            n = int(n)
            if n != 0:
                if n == 4:
                    roman = symbol[0] + symbol[1] + roman
                elif n == 9:
                    roman = symbol[0] + symbol[2] + roman
                else:
                    roman = symbol[0]*n + roman if n <= 3 else symbol[1] + symbol[0] * (n-5) + roman
        return roman
