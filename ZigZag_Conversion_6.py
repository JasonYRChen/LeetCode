class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # sort char in s into numRows part
        words = [''] * numRows
        cycle = 2*numRows-2 if 2*numRows-2 else 1
        for i, char in enumerate(s):
            row = i % cycle
            if row >= numRows:
                row = cycle - row
            words[row] += char
        return ''.join(words)
    
    # find the char and append right to the next char in word
    # def convert(self, s: str, numRows: int) -> str:
    #     word = ''
    #     section = 2 * numRows - 2  if 2*numRows-2 else 1
    #     start = 0
    #     idx, left, right = 0, 0, section
    #     for _ in range(len(s)):
    #         word += s[idx]
    #         idx += left if idx % section >= numRows else right
    #         if idx >= len(s):
    #             start -= 1
    #             left = 2 * abs(start)
    #             right = section - left if left < section else section
    #             idx = start + left
    #     return word

