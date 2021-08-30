class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        three_times = sum(set(nums)) * 3
        one_times = sum(nums)
        return (three_times - one_times) // 2

