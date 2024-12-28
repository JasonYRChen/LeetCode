class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # soluiton 1: O(n)
        squared = []
        left, right = 0, len(nums) - 1
        while left <= right:
            if abs(nums[left]) >= abs(nums[right]):
                squared.append(nums[left] ** 2)
                left += 1
            else:
                squared.append(nums[right] ** 2)
                right -= 1
        return squared[::-1]
            
        # solution 2: O(log n) + O(n)
#        idx = len(nums) - 1
#        mid = len(nums) // 2
#        while idx != mid:
#            if nums[mid] >= 0:
#                idx = mid
#                mid = idx // 2
#            else:
#                mid_temp = (mid + idx) // 2
#                mid = mid_temp if mid != mid_temp else mid_temp + 1

#        squared = []
#        left, right = idx - 1, idx
#        while left > -1 or right < len(nums):
#            if left == -1 or (right < len(nums) and abs(nums[left]) > abs(nums[right])):
#                squared.append(nums[right]**2)
#                right += 1
#            else:
#                squared.append(nums[left]**2)
#                left -= 1
#        return squared
