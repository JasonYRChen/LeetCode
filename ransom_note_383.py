class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = defaultdict(int)
        for char_r, char_m in zip_longest(ransomNote, magazine):
            counter[char_r] += 1
            counter[char_m] -= 1
        counter[None] = 0
        for value in counter.values():
            if value > 0:
                return False
        return True
