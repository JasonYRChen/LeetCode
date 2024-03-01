class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd = 1
        for even in range(0, len(nums), 2):
            if nums[even] % 2:
                while nums[odd] % 2:
                    odd += 2
                nums[even], nums[odd] = nums[odd], nums[even]
        return nums
        
"""
        evens = [nums[i] for i in range(len(nums)) if (i % 2) and not (nums[i] % 2)]
        odds = [nums[i] for i in range(len(nums)) if not (i % 2) and (nums[i] % 2)]
        for i in range(len(nums)):
            if (nums[i] % 2) ^ (i % 2):
                nums[i] = odds.pop() if i % 2 else evens.pop()
        return nums
"""
