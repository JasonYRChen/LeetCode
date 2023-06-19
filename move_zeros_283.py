class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #1 2*O(N) time, O(1) space
#        total = sum(nums)
#        insert = 0
#        for num in nums:
#            if num:
#                nums[insert] = num
#                insert += 1
#                total -= num
#            if not total:
#                break
#        for i in range(insert, len(nums)):
#            nums[i] = 0

        #2 O(N) time, O(1) space
        insert = 0
        for num in nums:
            if num:
                nums[insert] = num
                insert += 1
        for i in range(insert, len(nums)):
            nums[i] = 0
