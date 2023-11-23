class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        # less messer code, but increase running time in some heavily repeated digits cases
        numbers = []
        for num in range(left, right + 1):
            temp = num
            while temp:
                temp, residue = divmod(temp, 10)
                if not residue or num % residue:
                    break
            else:
                numbers.append(num)
        return numbers

        # using set to avoid repeated divider, but the code is a little messer
#        numbers = []
#        for num in range(left, right + 1):
#            digits = set()
#            temp = num
#            while temp:
#                temp, residue = divmod(temp, 10)
#                digits.add(residue)
#            for digit in digits:
#                if not digit or num % digit:
#                    break
#            else:
#                numbers.append(num)
#        return numbers
