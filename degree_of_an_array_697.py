class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        degree, min_len = 0, float('inf')
        buckets = defaultdict(list)
        for i in range(len(nums)):
            buckets[nums[i]].append(i)
        for bucket in buckets.values():
            new_degree, new_min_len = len(bucket), bucket[-1] - bucket[0] + 1
            if new_degree > degree or (new_degree == degree and new_min_len < min_len):
                degree, min_len = new_degree, new_min_len
        return min_len
