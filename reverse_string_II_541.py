class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        anchor = 0
        string = ''
        while anchor < len(s):
            string += s[anchor:anchor+k][::-1] + s[anchor+k:anchor+2*k]
            anchor += 2 * k 
        return string 
