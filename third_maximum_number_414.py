class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        array = [-float('inf')] * 3
        for num in nums:
            if num not in array:
                array[0], num = max(array[0], num), min(array[0], num)
                array[1], num = max(array[1], num), min(array[1], num)
                array[2], num = max(array[2], num), min(array[2], num)
        return array[0] if array[2] == -float('inf') else array[2]
