class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        i_stack = [0]
        result = [-1 for _ in range(len(nums))]
        for i in range(1, len(nums) * 2):
            i %= len(nums)
            while i_stack and nums[i] > nums[i_stack[-1]]:
                result[i_stack.pop()] = nums[i]
            i_stack.append(i)
        return result
