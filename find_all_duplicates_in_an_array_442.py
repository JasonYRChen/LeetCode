class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        result = []
        for num, count in counter.items():
            if count == 2:
                result.append(num)
        return result
