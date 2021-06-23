class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_dict = {}
        for i, num in enumerate(nums):
            if num in diff_dict:
                return [diff_dict[num], i]
            diff_dict[target-num] = i

