class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
    
        ## Another solution for pure Python
        # if not needle:
        #     return 0
        # for i, c in enumerate(haystack):
        #     if c == needle[0] and haystack[i:i+len(needle)] == needle:
        #         return i
        # return -1
                
