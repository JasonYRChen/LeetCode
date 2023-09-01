class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = ''.join(s.split('-'))[::-1].upper()
        new_s = s[:k]
        for i in range(1, len(s) // k + bool(len(s) % k)):
            new_s += '-' + s[i*k:(i+1)*k]
        return new_s[::-1]
