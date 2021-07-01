class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Pure Python solution
        k = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[k]:
                k += 1
                if k != i:
                    nums[k] = nums[i]
        return k + 1 if nums else 0
    
        # # Solution with maximize use of C, or, built-in functions
        # nums[:] = sorted(list(set(nums)))
        # return len(nums)

