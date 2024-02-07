class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        s_split = []
        total = 0
        for c in s:
            if c.isalpha():
                total += 1
            else:
                c = int(c)
                total *= c
            s_split.append(c)
            if total >= k:
                break
        
        while s_split:
            while isinstance(s_split[-1], int):
                total //= s_split.pop()
            k %= total
            if not k:
                return s_split[-1]
            total -= 1
            s_split.pop()
