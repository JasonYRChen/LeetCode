class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        max_steps = [len(matrix[0]), len(matrix)-1]
        step, max_step, accumulate = 0, 0, 0
        row = col = 0
        
        result = []
        for i in range(1, len(matrix) * len(matrix[0])+1):
            result.append(matrix[row][col])
            if (i - accumulate) == max_steps[max_step]:
                step = (step + 1) % 4
                accumulate += max_steps[max_step]
                max_steps[max_step] -= 1
                max_step = (max_step + 1) % 2
            row, col = row+steps[step][0], col+steps[step][1]
        return result

