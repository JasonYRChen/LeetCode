class Solution:
    def rob(self, nums) -> int:
        prev2_path1 = prev2_path2 = 0
        prev_path1 = nums[0] if len(nums) else 0
        prev_path2 = nums[1] if len(nums) > 1 else 0
        reward = max(prev_path1, prev_path2)
        for i in range(1, len(nums) - 1):
            prev2_path1, prev_path1 = prev_path1, nums[i] + max(prev2_path1, prev_path1 - nums[i-1])
            prev2_path2, prev_path2 = prev_path2, nums[i+1] + max(prev2_path2, prev_path2 - nums[i])
            reward = max(reward, prev_path1, prev_path2)
        return reward


if __name__ == '__main__':
    n = [1, 2, 3]
    print(Solution().rob(n))

