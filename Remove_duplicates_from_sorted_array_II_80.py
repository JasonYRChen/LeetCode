class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lead_i = check_i = 0
        while lead_i < len(nums) and (not lead_i or nums[lead_i] >= nums[lead_i-1]):
            if nums[check_i] != nums[lead_i]:
                lead_i, check_i = lead_i+1, lead_i
            elif lead_i - check_i == 2:
                nums[lead_i:] = nums[lead_i+1:]
            else:
                lead_i += 1
        return len(nums)
