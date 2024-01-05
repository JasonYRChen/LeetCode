class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        counter = {}
        for num in arr:
            counter[num] = 1
            for child in counter:
                if (other_child := num / child) in counter:
                    counter[num] += counter[child] * counter[other_child]
        return sum(v for v in counter.values()) % (10**9 + 7)
