class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Assume grid is a m x n matrix
        # Running time: O(mn), memory: O(n)
        dp = [0] * (len(obstacleGrid[0])+1)
        dp[1] = 1
        for row in range(len(obstacleGrid)):
            for col in range(len(obstacleGrid[0])):
                dp[col+1] = 0 if obstacleGrid[row][col] else dp[col] + dp[col+1]
        return dp[-1]
        
        
        # Running time: O(mn), memory: O(mn)
        dp = [[0] * (len(obstacleGrid[0])+1) for _ in range(len(obstacleGrid)+1)]
        dp[0][1] = 1
        for row in range(1, len(obstacleGrid)+1):
            for col in range(1, len(obstacleGrid[0])+1):
                dp[row][col] = 0 if obstacleGrid[row-1][col-1] else dp[row-1][col]+dp[row][col-1]
        return dp[-1][-1]
