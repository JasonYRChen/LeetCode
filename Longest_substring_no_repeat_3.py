class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index = {}
        start, length = 0, 0
        for i, char in enumerate(s):
            if char in index and index[char] >= start:
                start = index[char] + 1
            length = max(length, i - start + 1)
            index[char] = i
        return length
            
