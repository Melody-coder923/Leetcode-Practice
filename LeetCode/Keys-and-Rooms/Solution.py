1class Solution:
2    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
3        n=len(rooms) # how many rooms
4        visited=set()
5        #前后有依赖
6
7        def dfs(id, visited):
8            if id in visited:
9                return
10            visited.add(id)
11            for r in rooms[id]:
12                dfs(r,visited)
13            return visited
14        dfs(0,visited)
15        return len(visited)==len(rooms)