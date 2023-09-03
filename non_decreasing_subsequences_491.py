class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = set()
        for length in range(2, len(nums) + 1):
            for candidate in combinations(nums, length):
                if candidate not in result:
                    for i in range(1, len(candidate)):
                        if candidate[i] < candidate[i-1]:
                            break
                    else:
                        result.add(candidate)
        return result
