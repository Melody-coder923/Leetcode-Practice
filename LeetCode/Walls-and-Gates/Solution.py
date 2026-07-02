1class Solution:
2    def wallsAndGates(self, rooms: List[List[int]]) -> None:
3        """
4        Do not return anything, modify rooms in-place instead.
5        """
6        if not rooms or not rooms[0]:
7            return
8
9        m, n = len(rooms), len(rooms[0])
10        INF = 2147483647
11        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
12
13        q = deque()
14
15        
16        for i in range(m):
17            for j in range(n):
18                if rooms[i][j] == 0:
19                    q.append((i, j, 0))
20
21        while q:
22            x, y, level = q.popleft()
23
24            for dx, dy in directions:
25                nx, ny = x + dx, y + dy
26
27                if 0 <= nx < m and 0 <= ny < n and rooms[nx][ny] == INF:
28                    rooms[nx][ny] = level + 1
29                    q.append((nx, ny, level + 1))