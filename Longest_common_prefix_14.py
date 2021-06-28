class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        for candidates in zip(*strs):
            word = set(candidates)
            if len(word) == 1:
                prefix += word.pop()
            else:
                break
        return prefix
