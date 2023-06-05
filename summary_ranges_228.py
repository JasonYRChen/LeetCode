class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        start = 0
        while start < len(nums):
            end = start + 1
            while (end < len(nums)) and (nums[end] - nums[start] == end - start):
                end += 1
            if start == end - 1:
                ans.append(str(nums[start]))
            else:
                ans.append(f'{nums[start]}->{nums[end-1]}')
            start = end
        return ans
