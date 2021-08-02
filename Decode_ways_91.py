class Solution:
    def numDecodings(self, s: str) -> int:
        # This is a transformed Fibonacci series problem. Recall the classic Fibonacci question and think why.
        if s[0] == '0':
            return 0
        num = int(s)
        
        pre_ways, curr_ways = 0, 1
        while num // 10 or num % 10:
            num, digit = divmod(num, 10)
            if not digit:
                num, digit = divmod(num, 10)
                if digit not in {1, 2}:
                    return 0
                curr_ways, pre_ways = curr_ways, 0
            else:
                new_num = (num % 10) * 10 + digit
                curr_ways, pre_ways = curr_ways+pre_ways, curr_ways if 11 <= new_num <= 26 else 0
        return curr_ways

