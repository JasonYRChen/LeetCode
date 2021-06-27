class Solution:
    def myAtoi(self, s: str) -> int:
        sign, number = 1, 0
        allowed = {str(n) for n in range(10)} | {'+', '-', ' '}
        digit_after_sign, end_of_digit = True, False
        
        for i, c in enumerate(s):
            if c not in allowed or not digit_after_sign or end_of_digit:
                break
            if c.isdigit() and i+1 < len(s) and not s[i+1].isdigit():
                end_of_digit = True
            if c in {'+', '-'}:
                if i+1 < len(s) and not s[i+1].isdigit():
                    digit_after_sign = False
                else:
                    sign = 1 if c == '+' else -1
            elif c.isdigit():
                number = number * 10 + int(c)
                
        number *= sign
        return number if -2**31 <= number <= 2**31-1 else [0, 2**31-1, -2**31][sign]
            
