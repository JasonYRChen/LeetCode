class Solution:
    def countBits(self, n: int) -> List[int]:
        ones = [0]
        while len(ones) < n + 1:
            temp = [x+1 for x in ones]
            ones.extend(temp[:n+1-len(ones)])
        return ones
