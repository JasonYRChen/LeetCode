class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        inward = [len(nodes) for nodes in graph]
        reversemap = defaultdict(list)
        for i, nodes in enumerate(graph):
            for node in nodes:
                reversemap[node].append(i)

        result = []
        queue = [i for i in range(len(inward)) if not inward[i]]
        while queue:
            start = queue.pop()
            result.append(start)
            for end in reversemap[start]:
                inward[end] -= 1
                if not inward[end]:
                    queue.append(end)
        return sorted(result)

        # solution 2
#        safe = set() 
#        dq = deque([(i, set(nodes)) for i, nodes in enumerate(graph)])
#        while dq:
#            old_length = len(dq)
#            for _ in range(old_length):
#                node, nodes = dq.popleft()
#                if not (nodes - safe):
#                    safe.add(node)
#                else:
#                    dq.append((node, nodes))
#            if len(dq) == old_length:
#                break
#        return sorted(list(safe))
