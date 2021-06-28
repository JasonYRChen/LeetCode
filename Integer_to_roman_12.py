class Solution:
    def intToRoman(self, num: int) -> str:
        symbols, roman = 'IVXLCDM', ''
        for i, digit in enumerate(str(num)[::-1]):
            symbol = symbols[2*i:2*i+3]
            digit = int(digit)
            if digit != 0:
                if digit == 4:
                    roman = symbol[0] + symbol[1] + roman
                elif digit == 9:
                    roman = symbol[0] + symbol[2] + roman
                else:
                    roman = symbol[0]*digit + roman if digit <= 3 else symbol[1] + symbol[0] * (digit-5) + roman
        return roman
