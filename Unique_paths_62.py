class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Solution 1: dynamic programing. Time: O(mn), space: O(n)
        paths = [1] * n
        for i in range((m - 1) * n):
            idx = i % n
            if idx:
                paths[idx] += paths[idx-1]
        return paths[-1]
        
        # # Solution 2: using math solution (may not be a good choice if m or n is extremely large)
        # return int(factorial(m+n-2) / factorial(m-1) / factorial(n-1))
