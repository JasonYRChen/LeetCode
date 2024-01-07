class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        large = []
        start = 0
        for i in range(len(s) + 1):
            if i == len(s) or s[i] != s[start]:
                if i - start > 2:
                    large.append([start, i - 1])
                start = i
        return large
