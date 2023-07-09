class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index_s, index_t = 0, 0
        while index_s < len(s) and index_t < len(t):
            if s[index_s] == t[index_t]:
                index_s += 1
            index_t += 1
        if (len(s) == 0) or (index_s == len(s) and s[index_s-1] == t[index_t-1]):
            return True
        return False
