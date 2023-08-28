class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count = 0
        for size in s:
            if count == len(g):
                break
            if size >= g[count]:
                count += 1
        return count
