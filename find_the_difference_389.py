class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter = defaultdict(int)
        for char_s, char_t in zip_longest(s, t):
            counter[char_t] += 1
            counter[char_s] -= 1
        for char, value in counter.items():
            if value == 1:
                return char
