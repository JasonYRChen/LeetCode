class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        island = set()
        for r in range(len(grid)):
            for c in range(len(grid)):
                # the cascaded for loops will never end at which the first island is found by dfs, it will 
                # then find the second with bfs
                if grid[r][c]:
                    stack = [(r, c)]
                    # dfs for the first island
                    while stack:
                        r, c = stack.pop()
                        if grid[r][c]:
                            island.add((r, c))
                            grid[r][c] = 0
                            stack.extend([(r+i, c+j) for i, j in directions if 0 <= r+i < len(grid) and 0 <= c+j < len(grid) and grid[r+i][c+j]])

                    # reaching out to the second island from the first one via bfs
                    queue = deque(island)
                    steps = 0
                    while queue:
                        for _ in range(len(queue)):
                            r, c = queue.popleft()
                            explores = [(r+i, c+j) for i, j in directions if 0 <= r+i < len(grid) and 0 <= c+j < len(grid) and (r+i, c+j) not in island]
                            for r, c in explores:
                                if grid[r][c]:
                                    return steps
                                island.add((r, c))
                                queue.append((r, c))
                        steps += 1 # increment every bfs round
