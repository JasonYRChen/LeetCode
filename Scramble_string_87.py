class Solution:
    @lru_cache(maxsize=None)
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        
        if Counter(s1) == Counter(s2):
            for cut in range(1, len(s1)):
                if self.isScramble(s1[:cut], s2[-cut:]) and self.isScramble(s1[cut:], s2[:-cut]):
                    return True
                if self.isScramble(s1[:cut], s2[:cut]) and self.isScramble(s1[cut:], s2[cut:]):
                    return True
        return False
        
