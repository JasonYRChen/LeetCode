class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        small, large = 0, len(s)
        ans = []
        for c in s:
            if c == 'I':
                ans.append(small)
                small += 1
            else:
                ans.append(large)
                large -= 1
        ans.append(small)
        return ans
