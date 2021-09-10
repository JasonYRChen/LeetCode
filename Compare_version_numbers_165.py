from itertools import zip_longest


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1, version2 = version1.split('.'), version2.split('.')
        for num1, num2 in zip_longest(version1, version2):
            num1 = int(num1) if num1 else 0
            num2 = int(num2) if num2 else 0
            if num1 > num2:
                return 1
            if num1 < num2:
                return -1
        return 0


if __name__ == '__main__':
    import sys

    print(Solution().compareVersion(sys.argv[1], sys.argv[2]))

