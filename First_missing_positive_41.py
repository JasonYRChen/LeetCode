class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            exchange_i = nums[i] - 1
            if 0 <= exchange_i < len(nums) and nums[i] != nums[exchange_i]:
                nums[i], nums[exchange_i] = nums[exchange_i], nums[i]
            else:
                i += 1

        for i, n in enumerate(nums, 1):
            if n != i:
                return i
        return len(nums) + 1
