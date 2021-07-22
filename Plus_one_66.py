class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        idx = -1
        while -idx <= len(digits) and digits[idx] == 9:
            digits[idx] = 0
            idx -= 1
        if -idx > len(digits):
            return [1] + digits
        digits[idx] += 1
        return digits
        
        # # Solution 2: using int-str type transform. Time consuming but lesser code
        # txt = str(int(''.join(str(n) for n in digits)) + 1)
        # return [int(n) for n in list(txt)]
