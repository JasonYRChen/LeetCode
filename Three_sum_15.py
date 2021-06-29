class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # O(nlogn)
        ans = []  # to output
        used1 = set()
        for first in range(len(nums) - 2):
            if nums[first] > 0:
                break
            if nums[first] not in used1:
                used1.add(nums[first])
                candidates = set()
                prohibit = set()
                for second in range(first+1, len(nums)):
                    if nums[second] not in candidates:
                        candidates.add(-nums[first]-nums[second])
                    elif nums[second] not in prohibit:
                        prohibit.add(nums[second])
                        ans.append([nums[first], -nums[first]-nums[second], nums[second]])
        return ans
