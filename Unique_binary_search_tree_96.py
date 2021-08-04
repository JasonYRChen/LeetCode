class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1] + [0] * n
        for index in range(1, n + 1):
            for left in range(index):
                right = index - 1 - left
                dp[index] += dp[left] * dp[right]
        return dp[-1]

