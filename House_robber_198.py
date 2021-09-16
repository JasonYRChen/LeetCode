class Solution:
    def rob(self, nums: list) -> int:
        prev_sum = prev_sum2 = 0
        last_num = 0
        max_value = 0
        for num in nums:
            current = max(num + prev_sum2, num + prev_sum - last_num)
            max_value = max(max_value, current)
            prev_sum2, prev_sum, last_num = prev_sum, current, num
        return max_value


if __name__ == '__main__':
    n = [2,7,9,3,1]
    print(Solution().rob(n))
        
