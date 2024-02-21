class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even_insert = 0
        for i in range(len(nums)):
            if not nums[i] % 2:
                nums[i], nums[even_insert] = nums[even_insert], nums[i]
                even_insert += 1
        return nums
