class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        dq = deque([0])
        remained = set(range(len(graph)))
        set1, set2 = {0}, set()
        while dq or remained:
            if not dq:
                dq.append(remained.pop())
            node = dq.popleft()
            set1, set2 = (set1, set2) if node in set1 else (set2, set1)

            for linked in graph[node]:
                if linked in set1:
                    return False
                if linked not in set2:
                    set2.add(linked)
                    dq.append(linked)
                    remained.discard(linked)
        return True
