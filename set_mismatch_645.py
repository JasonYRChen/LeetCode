class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        found = set()
        for n in nums:
            if n in found:
                duplicated = n
            else:
                found.add(n)
        return [duplicated, sum(range(len(nums)+1)) - sum(found)]
