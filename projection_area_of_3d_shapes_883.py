class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        total = sum(max(r) for r in grid) + sum(max(r) for r in zip(*grid))
        total += sum(sum(map(lambda x: 1 if x else 0, r)) for r in grid)
        return total
