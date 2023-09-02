class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_num, count = 0, 0
        for num in nums:
            if num:
                count += 1
            else:
                max_num = max(max_num, count)
                count = 0
        return max(max_num, count)
