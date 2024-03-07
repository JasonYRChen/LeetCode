class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for r in range(1, len(matrix)):
            for c in range(len(matrix[0])):
                matrix[r][c] += min([matrix[r-1][c+i] for i in [-1, 0, 1] if 0 <= c+i < len(matrix)])
        return min(matrix[-1])
