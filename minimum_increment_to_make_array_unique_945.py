class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        # solution 1. bucket sort, may be more memory consuming than solution 2 but faster
        bucket = [0 for _ in range(max(nums) + 1)]
        for n in nums:
            bucket[n] += 1

        steps = 0
        for i in range(len(bucket) - 1):
            if bucket[i] > 1:
                excess = bucket[i] - 1
                bucket[i+1] += excess
                steps += excess
        if bucket[-1] > 1:
            steps += bucket[-1] * (bucket[-1] - 1) // 2
        return steps

        
        # solution 2. 
#        counter = defaultdict(int)
#        for n in nums:
#            counter[n] += 1

#        steps = 0
#        keys = list(counter.keys())
#        heapq.heapify(keys)
#        while keys:
#            key = heapq.heappop(keys)
#            if counter[key] > 1:
#                excess = counter[key] - 1
#                steps += excess
#                if key + 1 not in counter:
#                    heapq.heappush(keys, key + 1)
#                counter[key+1] += excess
#        return steps
