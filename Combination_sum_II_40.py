class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return list(self.comb(candidates, target, 0, []))
        
    def comb(self, candidates, target, start, array):
        for i in range(start, len(candidates)):
            if i == start or candidates[i] != candidates[i-1]:
                if candidates[i] > target:
                    break
                new_array = array + [candidates[i]]
                if candidates[i] == target:
                    yield new_array
                else:
                    yield from self.comb(candidates, target-candidates[i], i+1, new_array)
