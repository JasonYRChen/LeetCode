class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        nums = [str(i) for i in nums]
        if len(nums) < 3:
            return f"{'/'.join(nums)}"
        return f"{nums[0]}/({'/'.join(nums[1:])})"
