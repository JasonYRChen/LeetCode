class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = [[x**2+y**2, i] for i, (x, y) in enumerate(points)]
        distance.sort()
        return [points[i[1]] for i in distance[:k]]
