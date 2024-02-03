class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stops = 0
        fuels = []
        stations.append([target, 0])
        for station, fuel in stations:
            if startFuel < target:
                while startFuel < station and fuels:
                    startFuel -= heapq.heappop(fuels)
                    stops += 1
                if startFuel >= station:
                    heapq.heappush(fuels, -fuel)
        return stops if startFuel >= target else -1
