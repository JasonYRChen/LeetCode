class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return list(self.permute(nums, []))
        
    def permute(self, nums, saving):
        if not nums:
            yield saving
        else:
            used = set()
            for i, num in enumerate(nums):
                if num not in used:
                    used.add(num)
                    yield from self.permute(nums[:i]+nums[i+1:], saving+[num])
