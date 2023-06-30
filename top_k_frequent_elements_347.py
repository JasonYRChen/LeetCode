class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1
        return heapq.nlargest(k, counter.keys(), key=lambda x: counter[x])
