class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        q = 0
        sign = 1 if not ((dividend >= 0) ^ (divisor >= 0)) else -1
        dividend, divisor = abs(dividend), [abs(divisor)]
        
        while dividend - divisor[-1] > 0:
            divisor.append(divisor[-1] + divisor[-1])
        
        idx = len(divisor) - 1
        while dividend > 0 and idx > -1:
            if dividend >= divisor[idx]:
                dividend -= divisor[idx]
                q += 2**idx
            else:
                idx -= 1
        result = sign * q if -2**31 <= sign * q <= 2**31-1 else 2**31-1
        return result
