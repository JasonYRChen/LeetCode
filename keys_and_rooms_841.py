class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        stack = [0]
        while stack:
            room = stack.pop()
            visited.add(room)
            stack.extend(set(rooms[room]) - visited)
        return len(rooms) == len(visited)
