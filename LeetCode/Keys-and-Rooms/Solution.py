1class Solution:
2    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
3        visited=set()
4        q=deque([0])
5        visited.add(0)
6        while q:
7            room=q.popleft()
8            for key in rooms[room]:
9                if key not in visited:
10                    visited.add(key)
11                    q.append(key)    
12        return len(visited)==len(rooms)