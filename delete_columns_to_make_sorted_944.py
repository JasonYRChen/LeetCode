class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # Let m = len(strs), n = len(strs[0])
        # Solution 1. O(m*n) running time. But pure Python code is slower than solution 2.
        total = 0
        for c in range(len(strs[0])):
            for r in range(1, len(strs)):
                if strs[r][c] < strs[r-1][c]:
                    total += 1
                    break
        return total

        # Solution 2. O(m*log(m)*n) running time. But with the help of C under the hood, this is faster
#        total = 0
#        for s in zip(*strs):
#            total += list(s) != sorted(s)
#        return total
