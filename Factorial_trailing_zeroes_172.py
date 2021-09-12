class Solution:
    def trailingZeroes(self, n: int) -> int:
        times = 0
        while n >= 5:
            n //= 5 
            times += n
        return times


if __name__ == '__main__':
    import sys

    print(Solution().trailingZeroes(int(sys.argv[1])))

