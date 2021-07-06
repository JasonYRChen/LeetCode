class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        mid = (0 + len(nums)) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            return self.searchInsert(nums[:mid], target)
        return mid + 1 + self.searchInsert(nums[mid+1:], target)
        
        # Solution 2: use bisect module
        # return bisect_left(nums, target)
