class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        steps = ((0, 1), (1, 0), (0, -1), (-1, 0))
        max_steps = [n, n-1]
        step = max_step = row = col = accumulate = 0
        
        for i in range(1, n*n+1):
            matrix[row][col] = i
            if (i - accumulate) == max_steps[max_step]:
                accumulate += max_steps[max_step]
                max_steps[max_step] -= 1
                step = (step + 1) % 4
                max_step = (max_step + 1) % 2
            row, col = row+steps[step][0], col+steps[step][1]
        return matrix

