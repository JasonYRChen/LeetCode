class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        pixels = 0
        for c in s:
            space = widths[ord(c) - ord('a')]
            lines += 1 if pixels + space > 100 else 0
            pixels = pixels + space if pixels + space <= 100 else space
        return lines, pixels
