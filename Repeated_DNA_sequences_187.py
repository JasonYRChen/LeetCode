from collections import defaultdict
from bisect import bisect_left


class Solution:
    def findRepeatedDnaSequences(self, s: str):
        ans = []
        visited  ={}
        for i in range(len(s) - 9):
            string = s[i:i+10]
            if string not in visited:
                visited[string] = 1
            elif visited[string]:
                ans.append(string)
                visited[string] = 0
        return ans


if __name__ == '__main__':
    import sys

    print(Solution().findRepeatedDnaSequences(sys.argv[1]))

