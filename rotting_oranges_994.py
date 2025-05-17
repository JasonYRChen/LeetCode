class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        fresh = set()
        rotting = deque()
        minute = 0

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    fresh.add((r, c))
                elif grid[r][c] == 2:
                    rotting.append((r, c))
        
        while rotting:
            time = 0
            for _ in range(len(rotting)):
                r, c = rotting.popleft()
                for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    p_r, p_c = r + x, c + y
                    if 0 <= p_c <= col and 0 <= p_r <= row and \
                       (p_r, p_c) in fresh:
                        fresh.remove((p_r, p_c))
                        rotting.append((p_r, p_c))
                        time = 1
            minute += time

        return minute if not fresh else -1
