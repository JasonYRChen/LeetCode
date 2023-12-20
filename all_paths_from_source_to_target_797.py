class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        dq = deque([[0]])
        while dq:
            path = dq.popleft()
            for node in graph[path[-1]]:
                new_path = path.copy()
                new_path.append(node)
                if node == len(graph) - 1:
                    result.append(new_path)
                else:
                    dq.append(new_path)
        return result
