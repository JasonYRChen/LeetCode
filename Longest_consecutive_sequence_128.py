class Solution:
    def longestConsecutive(self, nums) -> int:
        # Solution 1. Running time: O(n)
        nums = set(nums)
        max_length = 0
       
        while nums:
            num = nums.pop()
            left = right = 1
            while num - left in nums:
                nums.remove(num - left)
                left += 1
            while num + right in nums:
                nums.remove(num + right)
                right += 1
            max_length = max(max_length, left + right - 1)
        return max_length

#        Solution 2. Running time: O(nlgn)
#        nums.sort()
#        max_length = 1 if nums else 0
#        start = 0
#        for i in range(1, len(nums)):
#            diff = nums[i] - nums[i-1]
#            if diff > 1 or diff == 0:
#                max_length = max(max_length, i - start)
#                start = i if diff else start + 1
#            else:
#                max_length = max(max_length, i - start + 1)
#        return max_length


if __name__ == '__main__':
    nums = [9,1,-3,2,4,8,3,-1,6,-2,-4,7]
    print(Solution().longestConsecutive(nums))

