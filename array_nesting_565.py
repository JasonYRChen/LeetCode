class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_num = 0
        while nums_set:
            temp_num = 1
            i = nums[nums_set.pop()]
            while i in nums_set:
                temp_num += 1
                nums_set.remove(i)
                i = nums[i]
            max_num = max(max_num, temp_num)
        return max_num
