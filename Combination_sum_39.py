class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return list(self.comb(candidates, target, 0, []))
    
    def comb(self, candidates, target, start, array):
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                break
            times, remain = divmod(target, candidates[i])
            if not remain:
                yield array + [candidates[i]] * times
            j = 0
            while j < times:
                new_target = target - candidates[i] * (times - j)
                new_array = array + [candidates[i]] * (times - j)
                yield from self.comb(candidates, new_target, i+1, new_array)
                j += 1
        
    ## Solution 2: same idea as above but slower 
    ##             because of not considering target = int.* candidate[i] directly
    # def comb(self, candidates, target, start, array):
    #     for i in range(start, len(candidates)):
    #         if candidates[i] > target:
    #             break
    #         new_array = array + [candidates[i]]
    #         if candidates[i] == target:
    #             yield new_array
    #         else:
    #             new_target = target - candidates[i]
    #             yield from self.comb(candidates, new_target, i, new_array)
        
