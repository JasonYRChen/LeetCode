class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            if n == 1:
                return True
            visited.add(n)
            temp = 0
            while n:
                n, remainder = divmod(n, 10)
                temp += remainder ** 2
            n = temp
        return False


if __name__ == '__main__':
    import sys

    print(Solution().isHappy(int(sys.argv[1])))

