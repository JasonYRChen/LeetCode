class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        num = 0
        divisible = []
        for n in nums:
            num = num * 2 + n
            divisible.append(not(num % 5))
        return divisible
