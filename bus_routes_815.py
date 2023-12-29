class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        stop_route = defaultdict(list)
        for route, stops in enumerate(routes):
            for stop in stops:
                stop_route[stop].append(route)

        buses = 0
        dq = deque(stop_route[source])
        traversed_stops = {source}
        traversed_routes = {i for i in stop_route[source]}
        while dq:
            buses += 1
            for _ in range(len(dq)):
                route = dq.popleft()
                for stop in routes[route]:
                    if stop == target:
                        return buses
                    if stop not in traversed_stops:
                        traversed_stops.add(stop)
                        for route in stop_route[stop]:
                            if route not in traversed_routes:
                                traversed_routes.add(route)
                                dq.append(route)
        return -1
