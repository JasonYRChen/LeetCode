class Solution:
    def partition(self, s: str):
        palindrome_index = []
        for end in range(len(s)):
            for start in range(len(palindrome_index)):
                word = s[start:end+1]
                if word == word[::-1]:
                    palindrome_index[start].append(end)
            palindrome_index.append([end])
        return [array for array in self.combinations(s, palindrome_index, [])]

    def combinations(self, s, palindrome_index, result, start=0):
        for end in palindrome_index[start]:
            new_result = result + [s[start: end+1]]
            if end == len(palindrome_index) - 1:
                yield new_result 
            else:
                yield from self.combinations(s, palindrome_index, new_result, end+1)


if __name__ == '__main__':
    import sys

    print(Solution().partition(sys.argv[1]))

