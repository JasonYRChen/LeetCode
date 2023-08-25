class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = {i for i in range(1, len(nums) + 1)}
        for i in nums:
            result.discard(i)
        return result
