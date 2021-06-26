class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, length = 0, 0
        for i in range(len(s)):
            even_start = i - length
            odd_start = i - length - 1
            odd_s, even_s = s[odd_start:i+1], s[even_start:i+1]
            if odd_start >= 0 and odd_s == odd_s[::-1]:
                start = odd_start
                length += 2
            elif even_start >= 0 and even_s == even_s[::-1]:
                start = even_start
                length += 1
        return s[start:start+length]
        
