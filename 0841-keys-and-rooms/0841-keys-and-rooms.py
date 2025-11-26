class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited=set()
        def dfs(key,visited):
            if key in visited:
                return 
            visited.add(key)
            for key in rooms[key]:
                dfs(key,visited)
        dfs(0,visited)
        return len(visited)==len(rooms)