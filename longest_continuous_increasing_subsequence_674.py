class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        max_len = 1
        start = 0
        i = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                max_len = max(max_len, i - start)
                start = i
        return max(max_len, i - start + 1)
