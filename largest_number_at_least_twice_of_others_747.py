class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_index, twice_index = 0, 0
        for i in range(1, len(nums)):
            if nums[i] > nums[max_index]:
                twice_index = i if nums[i] >= 2 * nums[max_index] else -1
                max_index = i
            else:
                twice_index = twice_index if nums[max_index] >= 2 * nums[i] else -1
        return twice_index
