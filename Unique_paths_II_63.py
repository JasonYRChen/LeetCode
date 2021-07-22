class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        # Solution 1. dynamic programming. Time: O(mn), space: O(n)
        if grid[0][0]:
            return 0
        
        g = [1] + [0] * (len(grid[0]) - 1)
        for row in range(len(grid)):
            g[0] = 1 if g[0] and not grid[row][0] else 0
            for col in range(1, len(grid[0])):
                g[col] = 0 if grid[row][col] else g[col] + g[col-1]
        return g[-1]
        
        ## Solution 2: dynamic programming. Time: O(mn), space: O(mn)
        # g = [[0] * len(grid[0]) for _ in range(len(grid)+1)]
        # g[0][0] = 1
        # for row in range(len(grid)):
        #     g[row+1][0] = 1 if g[row][0] and not grid[row][0] else 0
        #     for col in range(1, len(grid[0])):
        #         g[row+1][col] = 0 if grid[row][col] else g[row][col] + g[row+1][col-1]
        # return g[-1][-1]
