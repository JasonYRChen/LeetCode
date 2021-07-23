class Solution:
    def climbStairs(self, n: int) -> int:
        prev, curr = 0, 1
        for i in range(n):
            prev, curr = curr, curr + prev
        return curr

