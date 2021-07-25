class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [num for num in range(1, n+1)]
        return [ans for ans in self.combination(nums, 0, k, [])]
        
    def combination(self, nums, start, remain, result):
        if not remain:
            yield result
        else:
            while len(nums) - start >= remain:
                yield from self.combination(nums, start+1, remain-1, result+[nums[start]])
                start += 1
