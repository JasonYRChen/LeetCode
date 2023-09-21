class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        time = [sum([int(n) * m for n, m in zip(t.split(':'), (60, 1))]) for t in  timePoints]
        time.sort()
        time.append(time[0] + 24 * 60)
        min_diff = float('inf')
        for i in range(1, len(time)):
            min_diff = min(min_diff, time[i] - time[i-1])
        return min_diff
