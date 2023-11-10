class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count = 0
        left = right = 0
        for i in range(len(s)):
            if s[i] != s[left] and right == left:
                right = i
            elif s[i] == s[left] and right != left:
                count += min(right - left, i - right)
                left, right = right, i
        count += min(right - left, i + 1 - right)
        return count
