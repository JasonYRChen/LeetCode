class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # solution 2:
        total = 0
        left = 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[left+1] - nums[left]:
                total += (i+1) - left - 3 + 1
            else:
                left = i - 1
        return total


        # solution 1:
#        total = 0
#        left = 0
#        for i in range(1, len(nums)):
#            if (nums[i] - nums[i-1] != nums[left+1] - nums[left]) and (i - left >= 3):
#                # valid arithmetic subarray
#                total += sum(range(i - left - 3 + 2))
#                left = i - 1
#            elif (i - left == 2) and (nums[i] - nums[i-1] != nums[i-1] - nums[left]):
#                # invalide arithmetic subarray, renew 'left'
#                left += 1
#
#        # check 'left', there could be arithmetic array unchecked after for loop
#        if len(nums) > 1 and (nums[-1] - nums[-2] == nums[left+1] - nums[left]) and ((len(nums) - left) >= 3):
#            total += sum(range(len(nums) - left - 3 + 2))
#        
#        return total
