class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # solution 1
        return s in (s + s)[1:-1]
        
        # solution 2
#        for step in range(1, len(s)//2 + 1):
#            partition, is_nonzero = divmod(len(s), step)
#            if not is_nonzero and (s[:step] * partition == s):
#                return True
#        return False
