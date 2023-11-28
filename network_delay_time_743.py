class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        lapse = 0
        nodes_found = set()
        nodes = defaultdict(list)
        for source, target, time in times:
            nodes[source].append((time, target))

        heap = [(0, k)]
        while heap:
            time, number = heapq.heappop(heap)
            if number not in nodes_found:
                nodes_found.add(number)
                lapse = time
                for t, target in nodes[number]:
                    if target not in nodes_found:
                        heapq.heappush(heap, (lapse + t, target))
        return lapse if len(nodes_found) == n else -1



"""
        lapse = 0
        nodes = defaultdict(list)
        for source, target, time in times:
            nodes[source].append((time, target))
        heap = nodes[k]
        nodes_found = {k} if heap else set()
        heapq.heapify(heap)
        while heap and len(nodes_found) != n:
            time, target = heapq.heappop(heap)
            if target not in nodes_found:
                lapse += time
                heap = list(map(lambda x: (x[0] - time, x[1]), heap))
                nodes_found.add(target)
                for node in nodes[target]:
                    heapq.heappush(heap, node)
        return lapse if len(nodes_found) == n else -1
"""
