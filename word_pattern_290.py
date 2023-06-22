class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        words = s.split()
        if len(pattern) != len(words):
            return False
            
        for p, w in zip(pattern, words):
            d[p] = w
        d = {w:p for p, w in d.items()}
        for p, w in zip(pattern, words):
            if w not in d or d[w] != p:
                return False
        return True
