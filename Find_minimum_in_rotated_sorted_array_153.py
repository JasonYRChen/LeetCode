class Solution:
    def findMin(self, nums) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= nums[left] > nums[right]: 
                left = mid + 1
            else:
                if nums[mid] < nums[mid-1]:  # This if statement is not necessary, but
                    return nums[mid]         # it can accelerate the searching by chance
                right = mid
        return nums[left]

