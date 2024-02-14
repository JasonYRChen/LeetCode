class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        prev = nums[0]
        less = True
        greater = True
        for n in nums:
            if n < prev:
                greater = False
            elif n > prev:
                less = False
            prev = n
        return less or greater
