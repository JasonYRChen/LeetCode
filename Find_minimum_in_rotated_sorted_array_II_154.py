class Solution:
    def findMin(self, nums) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            elif nums[right] >= nums[mid] or nums[left] > nums[mid]:
                right = mid
            elif nums[right] < nums[mid]:
                left = mid + 1
        return nums[left]

