from collections import defaultdict


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        keys = set(t)
        t_indices = defaultdict(list)
        for i, c in enumerate(t):
            t_indices[c].append(i)
        dp = [1] + [0] * len(t)
        
        for c in s:
            if c in keys:
                for index in t_indices[c][::-1]:
                    dp[index+1] += dp[index]
        return dp[-1]

