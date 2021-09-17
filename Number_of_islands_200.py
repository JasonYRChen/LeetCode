class Solution:
    def numIslands(self, grid) -> int:
        # Solution 1. O(mn) time, O(1) space (but may increase to O(mn) at some moments).
        # Disadvantage is messing the original data.
        islands = 0
        len_row, len_col = len(grid), len(grid[0])
        for row in range(len_row):
            for col in range(len_col):
                if grid[row][col] == '1':
                    islands += 1
                    stack = [(row, col)]
                    while stack:
                        coord_r, coord_c = stack.pop()
                        grid[coord_r][coord_c] = '0'
                        candidates = [(coord_r+1, coord_c), (coord_r-1, coord_c),
                                      (coord_r, coord_c+1), (coord_r, coord_c-1)]
                        for coord in candidates:
                            if 0 <= coord[0] < len_row and 0 <= coord[1] < len_col and \
                               grid[coord[0]][coord[1]] == '1':
                                stack.append(coord)
        return islands

#        # Solution 2. O(mn) time, O(mn) space. Advantage is not changing original data
#        islands = 0
#        visited = set()
#        len_row, len_col = len(grid), len(grid[0])
#        for row in range(len_row):
#            for col in range(len_col):
#                if (row, col) not in visited and grid[row][col] == '1':
#                    islands += 1
#                    stack = [(row, col)]
#                    while stack:
#                        point_row, point_col = stack.pop()
#                        visited.add((point_row, point_col))
#                        candidates = [(point_row+1, point_col), (point_row-1, point_col),
#                                      (point_row, point_col+1), (point_row, point_col-1)]
#                        for coord in candidates: 
#                            if 0 <= coord[0] < len_row and 0 <= coord[1] < len_col and \
#                               grid[coord[0]][coord[1]] == '1' and coord not in visited:
#                                stack.append(coord)
#        return islands


if __name__ == '__main__':
    g = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

    print(Solution().numIslands(g))

