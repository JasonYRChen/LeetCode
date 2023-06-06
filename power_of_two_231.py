class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n > 1:
            n, r = divmod(n, 2)
            if n >= 1 and r:
                return False
        return True if n == 1 else False


if __name__ == '__main__':
    for n in range(10):
        result = Solution.isPowerOfTwo('a', n)
        print(f"{n} {'is' if result else 'is not'} power of 2")
