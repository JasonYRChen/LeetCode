class Solution:
    def rotate(self, nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Solution 1. O(n) running time, O(1)space
        if not k:
            return
        repeat, not_divided = divmod(len(nums), k)
        index, value = 0, nums[0]
        for i in range(len(nums)):
            if not not_divided and not (i % repeat):
                index = i // repeat
                value = nums[index]
            index = (index + k) % len(nums)
            nums[index], value = value, nums[index]

#        # Solution 2. O(n) running time, O(n) space
#        k = k % len(nums)
#        if not k:
#            return
#        nums[:k], nums[k:] = nums[-k:], nums[:-k]


if __name__ == '__main__':
    n = [1,2,3,4,5,6,7]
    k = 3
    Solution().rotate(n, k)
    print(n)

