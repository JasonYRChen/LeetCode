class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # Solution 1: this is an extended problem of previous one 'Largest Rectangle in Histogram'
        area = 0
        heights = [0 for _ in range(len(matrix[0])+1)] if matrix else []
        for array in matrix:
            for i, char in enumerate(array):
                heights[i] = heights[i] + 1 if char == '1' else 0
                
            indices = [-1]
            for i in range(len(heights)):
                while heights[i] < heights[indices[-1]]:
                    height = heights[indices.pop()]
                    width = i - indices[-1] - 1
                    area = max(area, height * width)
                indices.append(i)
        return area

    
    # # Solution 2: brutal method, testing maximum rectangle expanding toward right and low at each point
    # def maximalRectangle(self, matrix: List[List[str]]) -> int:
    #     if not matrix:
    #         return 0
    #     width, height = len(matrix[0]), len(matrix)
    #     area = 0
    #     for row in range(height):
    #         for col in range(width):
    #             if matrix[row][col] == '1':
    #                 try:
    #                     col_idx = matrix[row][col:].index('0') + col
    #                 except:
    #                     col_idx = width
    #                 while col_idx > col:
    #                     if (col_idx - col) * (height - row) <= area:
    #                         break
    #                     row_idx = row + 1
    #                     while row_idx < height:
    #                         if '0' not in matrix[row_idx][col:col_idx]:
    #                             row_idx += 1
    #                         else:
    #                             break
    #                     new_area = (row_idx - row) * (col_idx - col)
    #                     area = max(area, new_area)
    #                     col_idx -= 1
    #     return area
