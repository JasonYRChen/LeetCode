class Solution:
#    def numDecodings(self, s: str) -> int:
#        # This is a transformed Fibonacci series problem. Recall the classic Fibonacci question and think why.
#        if s[0] == '0':
#            return 0
#        num = int(s)
#        
#        pre_ways, curr_ways = 0, 1
#        while num // 10 or num % 10:
#            num, digit = divmod(num, 10)
#            if not digit:
#                num, digit = divmod(num, 10)
#                if digit not in {1, 2}:
#                    return 0
#                curr_ways, pre_ways = curr_ways, 0
#            else:
#                new_num = (num % 10) * 10 + digit
#                curr_ways, pre_ways = curr_ways+pre_ways, curr_ways if 11 <= new_num <= 26 else 0
#        return curr_ways

    def numDecodings(self, s: str) -> int:
        # Solution 2
        if s[0] == '0':
            return 0
        pre_ways, curr_ways = 1, 1
        for i in range(1, len(s)):
            num = int(s[i-1:i+1])
            if s[i] == '0' and num not in {10, 20}:
                return 0
            
            temp_ways = curr_ways
            if s[i] == '0':
                temp_ways = 0
            if 10 <= num <= 26:
                curr_ways = temp_ways + pre_ways
            pre_ways = temp_ways
        return curr_ways

