class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # Solution 1. using dynamic programming
        dp = [1] + [0] * rowIndex
        for i in range(rowIndex):
            prev = dp[0]
            for index in range(1, i+2):
                dp[index], prev = dp[index] + prev, dp[index]
        return dp

#        # Solution 2. renew result every iteration.
#        result = [1]
#        for _ in range(rowIndex):
#            result = [1] + [result[i-1]+result[i] for i in range(1, len(result))] + [1]
#        return result

