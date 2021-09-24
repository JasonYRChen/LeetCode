class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        length = float('inf')
        start = 0
        for i, num in enumerate(nums):
            target -= num
            while target + nums[start] <= 0:
                target += nums[start]
                start += 1
            if target <= 0:
                length = min(length, i - start + 1)
        return length if length != float('inf') else 0


if __name__ == '__main__':
    t = 11
    n = [1, 1, 1, 1, 1, 1, 1, 1]
    print(Solution().minSubArrayLen(t, n))

