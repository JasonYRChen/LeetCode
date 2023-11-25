class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = Counter(nums)
        array = sorted([(k, k * v) for k, v in counter.items()])
        dp = [0 for _ in range(len(array) + 1)]
        dp[1] = array[0][1]
        for i in range(1, len(array)):
            if array[i][0] == array[i-1][0] + 1:
                dp[i+1] = max(dp[i], dp[i-1] + array[i][1])
            else:
                dp[i+1] = dp[i] + array[i][1]
        return dp[-1]
