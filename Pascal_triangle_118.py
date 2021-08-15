class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        for _ in range(1, numRows):
            last = result[-1]
            latest = [1] + [last[i-1]+last[i] for i in range(1, len(last))] + [1]
            result.append(latest)
        return result
