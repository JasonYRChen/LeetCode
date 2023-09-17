class Solution:
    def countArrangement(self, n: int) -> int:
        def perm_count(target, nums):
            result = 0
            for num in nums:
                if not ((target % num) and (num % target)):
                    if target == 1:
                        return 1
                    new_nums = nums - {num}
                    result += perm_count(target - 1, new_nums)
            return result

        nums = {i+1 for i in range(n)}
        return perm_count(n, nums)
