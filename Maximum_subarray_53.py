class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current, max_sum = 0, nums[0]
        for n in nums:
            current = current + n if current + n > 0 else 0
            max_sum = max(max_sum, current if current else n)
        return max_sum

