from collections import defaultdict


class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        if k > 0:
            nums_dict = {}
            for i, num in enumerate(nums):
                if num in nums_dict and i - nums_dict[num] <= k:
                    return True
                else:
                    nums_dict[num] = i
        return False


if __name__ == '__main__':
    n = [1, 2, 3, 1]
    k = 3
    print(Solution().containsNearbyDuplicate(n, k))

