class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        endtime = timeSeries[0] + duration - 1
        lapse = duration
        for i in range(1, len(timeSeries)):
            if endtime >= timeSeries[i]:
                lapse += timeSeries[i] - timeSeries[i-1]
                endtime += timeSeries[i] - timeSeries[i-1]
            else:
                lapse += duration
                endtime = timeSeries[i] + duration - 1
        return lapse
