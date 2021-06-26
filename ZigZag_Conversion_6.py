class Solution:
    def convert(self, s: str, numRows: int) -> str:
        words = [''] * numRows
        cycle = 2*numRows-2 if 2*numRows-2 else 1
        for i, char in enumerate(s):
            row = i % cycle
            if row >= numRows:
                row = cycle - row
            words[row] += char
        return ''.join(words)

