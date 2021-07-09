class Solution:
    def jump(self, nums: List[int]) -> int:
        count, max_step, step = 0, 0, 1
        for num in nums[:-1]:
            max_step = max(max_step-1, num)
            step -= 1
            if not step:
                count += 1
                step = max_step
        return count
