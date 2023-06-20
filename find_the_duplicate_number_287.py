class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        for k, v in counter.items():
            if v != 1:
                return k
