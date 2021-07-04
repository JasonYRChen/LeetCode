class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        switch1 = len(nums) - 2
        while switch1 > -2 and nums[switch1] >= nums[switch1+1]:
            switch1 -= 1
        if switch1 > -1:
            switch2 = self.bisect(nums, switch1+1, len(nums), nums[switch1])
            nums[switch1], nums[switch2] = nums[switch2], nums[switch1]
        left, right = switch1+1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
    def bisect(self, array, start, end, val):
        if end - start <= 1:
            return start        
        mid = (start + end) // 2
        start, end = (start, mid) if val >= array[mid] else (mid, end)
        return self.bisect(array, start, end, val)

