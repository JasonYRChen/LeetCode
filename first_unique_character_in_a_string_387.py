class Solution:
    def firstUniqChar(self, s: str) -> int:
        # This code only works on Python version with recorded dictionary building sequence 
        counter = {}
        for i, char in enumerate(s):
            if char in counter:
                counter[char] = -1
            else:
                counter[char] = i
        for value in counter.values():
            if value != -1:
                return value
        return value

        # This code works on all version of Python
        #counter = {}
        #for i, char in enumerate(s):
        #    if char in counter:
        #        counter[char] = math.inf
        #    else:
        #        counter[char] = i
        #
        #min_index = math.inf
        #for value in counter.values():
        #    min_index = min(min_index, value)
        #return min_index if min_index != math.inf else -1
