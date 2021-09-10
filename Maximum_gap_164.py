class Solution:
    def maximumGap(self, nums) -> int:
        # Solution 2. O(nlgn) with sort function
        nums.sort()
        
        gap = 0
        for i in range(1, len(nums)):
            gap = max(gap, nums[i] - nums[i-1])
        return gap


#        # Solution 1. O(n) running time, but slower than O(nlgn) solution with sort function
#        min_num, max_num = min(nums), max(nums)
#        if min_num == max_num:
#            return 0
#        interval = (max_num - min_num) / (len(nums) - 1) 
#        buckets = [[float('inf'), float('-inf')] for _ in range(len(nums))]
#        for num in nums:
#            index = int((num-min_num) / interval)
#            buckets[index][0] = min(buckets[index][0], num)
#            buckets[index][1] = max(buckets[index][1], num)
#
#        prev_max = min_num
#        gap = 0
#        for bucket in buckets:
#            if bucket[0] != float('inf'):
#                current_min, current_max = bucket[0], bucket[1]
#                gap = max(gap, current_min - prev_max)
#                prev_max = current_max
#        return gap


if __name__ == '__main__':
    n = [10]
    print(Solution().maximumGap(n))

