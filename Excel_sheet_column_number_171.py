class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        total = 0
        for char in columnTitle:
            total = total * 26 + ord(char) - ord('A') + 1
        return total


if __name__ == '__main__':
    import sys

    print(Solution().titleToNumber(sys.argv[1]))

