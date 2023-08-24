class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        total = 0
        for i in range(len(points)):
            distance = defaultdict(int)
            for j in range(len(points)):
                dis = (points[j][0] - points[i][0])**2 + (points[j][1] - points[i][1])**2
                distance[dis] += 1
            for num in distance.values():
                total += num * (num - 1)
        return total
