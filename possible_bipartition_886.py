class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        g1, g2 = set(), set()
        visited = set()
        seperates = defaultdict(set)
        for x, y in dislikes:
            seperates[x].add(y)
            seperates[y].add(x)
        for key, dislike in seperates.items():
            if key not in visited:
                candidates = {key}
                while candidates:
                    candidate = candidates.pop()
                    visited.add(candidate)
                    g1, g2 = (g1, g2) if candidate in g1 else (g2, g1)
                    g1.add(candidate)
                    for disliker in seperates[candidate]:
                        if disliker in g1:
                            return False
                        if disliker not in visited:
                            candidates.add(disliker)
                        g2.add(disliker)
        return True
