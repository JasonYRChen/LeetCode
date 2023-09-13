class Solution:
#    # Solution 1: use build-in function "functools.cache"
#    @cache
#    def fib(self, n: int) -> int:
#        if n < 2:
#            return n
#        return self.fib(n - 1) + self.fib(n - 2)


    # Solution 2: dynamic programming
    def fib(self, n: int) -> int:
        fib_array = [0, 1]
        for i in range(2, n + 1):
            fib_array.append(fib_array[i-1] + fib_array[i-2])
        return fib_array[n]
