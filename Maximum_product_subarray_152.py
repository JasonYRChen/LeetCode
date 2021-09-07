class Solution:
    def maxProduct(self, nums) -> int:
        min_product = max_product = 1
        result = nums[0]
        for num in nums:
            next_max_product, next_min_product = max_product * num, min_product * num
            max_product = max(next_max_product, num, next_min_product)
            min_product = min(next_max_product, num, next_min_product)
            result = max(result, max_product)
        return result

