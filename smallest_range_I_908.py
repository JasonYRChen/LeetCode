class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        diff = max(nums) - min(nums) - 2 * k
        return diff if diff >= 0 else 0
