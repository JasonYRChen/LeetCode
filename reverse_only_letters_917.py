class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        index = len(s) - 1
        output = ''
        for c in s:
            if c.isalpha():
                while not s[index].isalpha():
                    index -= 1
                c = s[index]
                index -= 1
            output += c
        return output
