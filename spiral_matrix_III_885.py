class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        coords = [[rStart, cStart]]
        base = 0
        steps = itertools.cycle([(0, 1), (1, 0), (0, -1), (-1, 0)])
        increments = itertools.cycle([1, 0])
        for inc, (step_r, step_c) in zip(increments, steps):
            base += inc
            for _ in range(base):
                rStart, cStart = rStart + step_r, cStart + step_c
                if (0 <= rStart < rows) and (0 <= cStart < cols):
                    coords.append([rStart, cStart])
                if len(coords) == rows * cols:
                    return coords
