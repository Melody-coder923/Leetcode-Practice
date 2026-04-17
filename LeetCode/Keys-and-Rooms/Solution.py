1class Solution:
2    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
3        visited = set()
4        def dfs(room):
5            if room in visited:
6                return
7            visited.add(room)
8            for key in rooms[room]:
9                dfs(key)
10
11        dfs(0)
12        return len(visited) == len(rooms)