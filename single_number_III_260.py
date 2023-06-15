class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        return [k for k, v in counter.items() if v == 1]
