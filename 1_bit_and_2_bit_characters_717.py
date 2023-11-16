class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        ans = 0
        while i < len(bits) - 1:
            i += 2 if bits[i] else 1
            ans = bits[i] if i < len(bits) else 1
        return not ans
