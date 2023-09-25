class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def linked(connections, city, scanned):
            for i in range(len(isConnected)):
                if connections[city][i] and i not in scanned:
                    scanned.add(i)
                    scanned = linked(connections, i, scanned)
            return scanned


        scanned = set()
        provinces = 0
        for i in range(len(isConnected)):
            if i not in scanned:
                scanned.add(i)
                provinces += 1
                scanned = linked(isConnected, i, scanned)
        return provinces
