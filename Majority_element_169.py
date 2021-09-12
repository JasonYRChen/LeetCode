class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Solution 1. O(n) time, O(1) space
        major, count = 0, 0
        for num in nums:
            if not count:
                major = num
    
            count += 1 if major == num else -1
        return major 

#        # Solution 2. O(n) time, O(n) space
#        counter = defaultdict(int)
#        times = len(nums) // 2 + len(nums) % 2
#        for num in nums:
#            counter[num] += 1
#            if counter[num] == times:
#                return num

