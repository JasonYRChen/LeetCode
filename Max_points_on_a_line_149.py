class Solution:
    def maxPoints(self, points) -> int:
        lines = {}
        visited = set()
        while points:
            to_update = set()
            point1 = points.pop()
            for point2 in points:
                feature = self.build_line(point1, point2)
                if feature not in visited:
                    if feature in lines:
                        lines[feature] += 1
                    else:
                        lines[feature] = 2
                        to_update.add(feature)                    
            visited.update(to_update) 
        return max(lines.values()) if lines else 1

    def build_line(self, point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        if x2 != x1:
            slope = ((y2-y1)/(x2-x1)).as_integer_ratio()
            intercept = ((x2*y1-x1*y2)/(x2-x1)).as_integer_ratio()
        else:
            slope, intercept = float('inf'), float('inf')
        return slope, intercept


if __name__ == '__main__':
    p = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    print(Solution().maxPoints(p))

