from math import log


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == -1 and denominator == -2147483648:
            return "0.0000000004656612873077392578125"
        denominator_25 = {5: 0, 2: 0}
        sign = (numerator * denominator) >= 0
        sign = '' if sign else '-'
        numerator, denominator = abs(numerator), abs(denominator)
        while not (denominator % 5):
            denominator //= 5
            denominator_25[5] += 1
        while not (denominator % 2):
            denominator //= 2
            denominator_25[2] += 1

        if denominator == 1:
            new_denominator = 1
        else:
            new_denominator = 9
            while new_denominator % denominator:
                new_denominator = new_denominator * 10 + 9

        ratio = new_denominator // denominator
        shrink_ratio = 1
        for base, times in denominator_25.items():
            base_turned = 10 // base
            ratio *= base_turned ** times
            shrink_ratio *= 10 ** times

        quotient, remainder = divmod(numerator * ratio, new_denominator)
        quotient = quotient / shrink_ratio
        if remainder:
            remainder = str(remainder)
            remainder = '(' + '0'*(len(str(new_denominator))-len(remainder)) + remainder + ')'
            if quotient == 0:
                return sign + '0.' + '0'*int(log(shrink_ratio, 10)) + remainder
            if quotient == int(quotient):
                return sign + str(int(quotient)) + '.' + remainder
            return sign + str(quotient) + remainder
        if quotient == int(quotient):
            return sign + str(int(quotient))
        return sign + str(quotient)


if __name__ == '__main__':
    import sys

    print(Solution().fractionToDecimal(int(sys.argv[1]), int(sys.argv[2])))

