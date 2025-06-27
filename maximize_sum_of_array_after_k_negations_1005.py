class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for _ in range(k):
            min_num = heapq.heappop(nums)
            heapq.heappush(nums, -min_num)
        return sum(nums)
