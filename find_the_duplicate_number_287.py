class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        for num in nums:
            if counter[num]:
                return num
            counter[num] += 1
