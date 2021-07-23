class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # This solution uses bucket sort
        counter = [0, 0, 0]
        for n in nums:
            counter[n] += 1
        
        start = 0
        for i in range(len(nums)):
            while counter[start] == 0:
                start += 1
            nums[i] = start
            counter[start] -= 1
        
#     # This solution uses in-sort with O(nlogn) time
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         self.sort(nums, 0, len(nums)-1)
        
#     def sort(self, nums, start, end):
#         if start >= end:
#             return
#         i_rand = randrange(start, end)
#         nums[i_rand], nums[end] = nums[end], nums[i_rand]
#         left, right = start, end - 1
#         while left <= right:
#             while left <= right and nums[left] <= nums[end]:
#                 left += 1
#             while left <= right and nums[right] > nums[end]:
#                 right -= 1
#             if left <= right:
#                 nums[left], nums[right] = nums[right], nums[left]
#         nums[left], nums[end] = nums[end], nums[left]
#         self.sort(nums, start, left-1)
#         self.sort(nums, left+1, end)

