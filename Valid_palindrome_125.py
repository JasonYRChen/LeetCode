class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Solution 1. O(len(s) + len(s.alnum())) running time
        s_array = [char.lower() for char in s if char.isalnum()]
        return s_array == s_array[::-1]

#        # Solution 2. Ideally O(len(s)) running time
#        left, right = 0, len(s) - 1
#        while left <= right:
#            while left <= right and not s[left].isalnum():
#                left += 1
#            while left <= right and not s[right].isalnum():
#                right -= 1
#            if left < right and s[left].lower() != s[right].lower():
#                return False
#            left += 1
#            right -= 1
#        return True

