class Solution:
    def minCut(self, s: str) -> int:
        # This question is like an extension of ladder problem only 1 or 2 steps can take
        # per round. Think why.
        for i in range(len(s)):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1 if i else 0

        cuts = [i for i in range(-1, len(s))]
        for idx in range(len(s)):
            r_odd = r_even = 0
            while 0 <= idx - r_odd and idx + r_odd < len(s) and \
                  s[idx-r_odd] == s[idx+r_odd]:
                cuts[idx+r_odd+1] = min(cuts[idx+r_odd+1], cuts[idx-r_odd] + 1)
                r_odd += 1
            while 0 <= idx - r_even and idx + r_even + 1 < len(s) and \
                  s[idx-r_even] == s[idx+r_even+1]:
                cuts[idx+r_even+2] = min(cuts[idx+r_even+2], cuts[idx-r_even] + 1)
                r_even += 1
        return cuts[-1]

#    def minCut(self, s: str) -> int:
#        palindrome_indices = []
#        for end in range(len(s)):
#            palindrome_indices.append(set())
#            for start in range(end + 1):
#                word = s[start:end+1]
#                if word == word[::-1]:
#                    palindrome_indices[end].add(start)
#
#        times = 0
#        queue = palindrome_indices[-1]
#        while queue:
#            temp = set()
#            for index in queue:
#                if index == 0:
#                    return times
#                temp.update(palindrome_indices[index-1])
#            queue = temp
#            times += 1


if __name__ == '__main__':
    import sys

    print(Solution().minCut(sys.argv[1]))

