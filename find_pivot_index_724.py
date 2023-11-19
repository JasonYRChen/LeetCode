class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        nums.append(0)
        left, right = 0, sum(nums[1:])
        for i in range(len(nums) - 1):
            if left == right:
                return i
            left, right = left + nums[i], right - nums[i+1]
        return -1
