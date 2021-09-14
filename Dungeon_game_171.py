class Solution:
    def calculateMinimumHP(self, dungeon) -> int:
        dp = [float('inf') for _ in range(len(dungeon[0]))]
        dp[-1] = 1
        for row in range(len(dungeon)-1, -1, -1):
            dp[-1] = max(dp[-1] - dungeon[row][-1], 1)
            for col in range(len(dungeon[0])-2, -1, -1):
                follower_min_hp = min(dp[col], dp[col+1])
                dp[col] = max(follower_min_hp-dungeon[row][col], 1)
        return dp[0]


if __name__ == '__main__':
    d = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
    print(Solution().calculateMinimumHP(d))

