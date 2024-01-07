class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def valid_coordinate(r, c):
            if r - 1 > -1:
                yield r - 1, c
            if r + 1 < len(grid):
                yield r + 1, c
            if c - 1 > -1:
                yield r, c - 1
            if c + 1 < len(grid[0]):
                yield r, c + 1


        # scan for island and label each independent island
        biggest = 1
        label = 2
        islands = {}
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    grid[row][col] = label
                    queue = [(row, col)]
                    area = 0
                    while queue:
                        r, c = queue.pop()
                        area += 1
                        for r, c in valid_coordinate(r, c):
                            if grid[r][c] == 1:
                                grid[r][c] = label
                                queue.append((r, c))

                    islands[label] = area
                    label += 1
                    biggest = max(area, biggest)
        
        # scan for sea grid which connect to any island as a bridge
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if not grid[row][col]:
                    lands = set()
                    for r, c in valid_coordinate(row, col):
                        if grid[r][c]:
                            lands.add(grid[r][c])
                    biggest = max(biggest, sum(islands[i] for i in lands) + 1)
        return biggest
