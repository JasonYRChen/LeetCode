class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = [nums]
        for _ in range(factorial(len(nums)) - 1):
            new = result[-1].copy()
            for anchor in range(len(new)-2, -1, -1):
                if new[anchor] < new[anchor+1]:
                    break
            for exchange in range(anchor+1, len(new)):
                if new[exchange] < new[anchor]:
                    exchange -= 1
                    break
            new[anchor], new[exchange] = new[exchange], new[anchor]
            left, right = anchor + 1, len(new) - 1
            while left < right:
                new[left], new[right] = new[right], new[left]
                left += 1
                right -= 1
            result.append(new)
        return result
                    
