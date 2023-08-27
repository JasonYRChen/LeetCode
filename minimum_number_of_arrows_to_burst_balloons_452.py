class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        arrows = 1
        arrow_position = 0
        for i in range(1, len(points)):
            if points[i][0] <= points[arrow_position][1]:
                points[arrow_position][1] = min(points[arrow_position][1], points[i][1])
            else:
                arrows += 1
                arrow_position = i
        return arrows
