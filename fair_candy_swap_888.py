class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        diff = (sum(aliceSizes) - sum(bobSizes)) / 2
        bobSet = set(bobSizes)
        for n in aliceSizes:
            if (n - diff) in bobSet:
                return [n, n - diff]
