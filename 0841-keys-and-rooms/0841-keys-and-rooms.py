class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited=set()
        q=deque([0])
        visited.add(0)
        while q:
            room=q.popleft()
            for key in rooms[room]:
                if key not in visited:
                    visited.add(key)
                    q.append(key)    
        return len(visited)==len(rooms)