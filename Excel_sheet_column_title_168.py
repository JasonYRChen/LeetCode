from string import ascii_uppercase as au


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ''
        while columnNumber > 0:
            columnNumber, remainder = divmod(columnNumber, 26)
            ans = au[remainder-1] + ans
            if not remainder:
                columnNumber -= 1
        return ans


if __name__ == '__main__':
    import sys

    print(Solution().convertToTitle(int(sys.argv[1])))

