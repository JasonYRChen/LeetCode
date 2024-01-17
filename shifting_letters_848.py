class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        shifts.append(0)
        chars = []
        for i in range(len(s)-1, -1, -1):
            shifts[i] += shifts[i+1]
            new_c = chr((ord(s[i]) - ord('a') + shifts[i]) % 26 + ord('a'))
            chars.append(new_c)
        return ''.join(chars[::-1])
