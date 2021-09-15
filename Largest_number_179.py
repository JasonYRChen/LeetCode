from random import randrange


class Solution:
    class _String(str):
        def __lt__(self, value):
            return self + value < value + self

    def largestNumber(self, nums) -> str:
        nums = sorted(map(self._String, nums), reverse=True)
        return '0' if nums[0] == '0' else ''.join(num for num in nums)

#    # Solution 2. build the same algorithm from scratch
#    def largestNumber(self, nums) -> str:
#        process_stack = [(0, len(nums) -1)] if len(nums) > 1 else []
#        while process_stack:
#            start, end = process_stack.pop()
#            left, right = start, end - 1
#            index = randrange(left, end)
#            nums[index], nums[end] = nums[end], nums[index]
#            while left <= right:
#                while left <= right and self.number_compare(nums[left], nums[end]):
#                    left += 1
#                while left <= right and self.number_compare(nums[end], nums[right]):
#                    right -= 1
#                if left <= right:
#                    nums[left], nums[right] = nums[right], nums[left]
#                    left += 1
#                    right -= 1
#            nums[left], nums[end] = nums[end], nums[left]
#            if left - 1 > start:
#                process_stack.append((start, left - 1))
#            if end > left + 1:
#                process_stack.append((left + 1, end))
#        return '0' if not nums[0] else ''.join(str(num) for num in nums)
#
#    def number_compare(self, num1, num2):
#        """
#        return if num1 >= num2
#        """
#        num1, num2 = str(num1), str(num2)
#        num1, num2 = int(num1+num2), int(num2+num1)
#        return True if num1 >= num2 else False


if __name__ == '__main__':
    import sys
    
    #num1, num2 = int(sys.argv[1]), int(sys.argv[2])
    #print(num1, '>=', num2, ':', Solution().number_compare(num1, num2))
    n = [0,0,1]
    print(Solution().largestNumber(n))

