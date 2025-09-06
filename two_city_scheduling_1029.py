class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        heapa = []
        heapb = []
        total = 0
        for cost in costs:
            if cost[0] > cost[1]:
                heapb.append(cost[0] - cost[1])
                total += cost[1]
            else:
                heapa.append(cost[1] - cost[0])
                total += cost[0]

        heap = heapa if len(heapa) > len(heapb) else heapb
        heapq.heapify(heap)
        for _ in range(abs(len(heapa) - len(heapb)) // 2):
            total += heapq.heappop(heap)
        return total
