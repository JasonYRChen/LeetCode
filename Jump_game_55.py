class Solution:
    def canJump(self, nums: List[int]) -> bool:
        remain = 0
        for num in nums[:-1]:
            remain = max(num, remain-1)
            if remain <= 0:
                return False
        return True
