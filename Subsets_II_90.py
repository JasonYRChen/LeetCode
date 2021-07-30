class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        final = [[]]
        for i in range(len(nums)):
            length = len(final)
            head = length-new_length if i and nums[i] == nums[i-1] else 0
            for start in range(head, length):
                final.append(final[start] + [nums[i]])
            new_length = len(final) - length
        return final

