1class Solution:
2    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
3        visited=set()
4        def dfs(key,visited):
5            if key in visited:
6                return 
7            visited.add(key)
8            for key in rooms[key]:
9                dfs(key,visited)
10        dfs(0,visited)
11        return len(visited)==len(rooms)