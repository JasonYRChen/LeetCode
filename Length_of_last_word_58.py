class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        array = s.split()
        return len(array[-1]) if array else 0
        
        ## Solution 2: not using Python build-in function
        # length = final = 0
        # for c in s:
        #     if c != ' ':
        #         length += 1
        #     else:
        #         if length:
        #             final = length
        #         length = 0
        # return length if length else final

