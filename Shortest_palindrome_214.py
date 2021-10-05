class Solution:
    def shortestPalindrome(self, s: str) -> str:
        pivot, is_odd = divmod(len(s), 2)
        for pivot in range(pivot, -1, -1):
            right_bound = 2 * pivot + 1
            for right_bound in (2*pivot+1, 2*pivot):
                if s[:right_bound]== s[:right_bound][::-1]:
                    return s[right_bound:][::-1] + s
            

if __name__ == '__main__':
    import sys

    print(Solution().shortestPalindrome(sys.argv[1]))

