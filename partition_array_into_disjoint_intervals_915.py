class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        anchor = biggest = nums[0]
        end = 0
        for i in range(len(nums)):
            if nums[i] > biggest:
                biggest = nums[i]
            elif nums[i] < anchor:
                anchor = biggest
                end = i
        return end + 1
