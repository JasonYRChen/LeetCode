class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_total = total = sum(nums[:k])
        for i in range(k, len(nums)):
            total += nums[i] - nums[i-k]
            max_total = max(max_total, total)
        return max_total / k
