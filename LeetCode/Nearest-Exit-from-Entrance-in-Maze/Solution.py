1class Solution:
2    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
3        m, n = len(maze), len(maze[0])
4        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
5        q = deque([(entrance[0], entrance[1], 0)])  # row, col, steps
6        maze[entrance[0]][entrance[1]] = "+" 
7        
8        while q:
9            x, y, steps = q.popleft()
10            # 只要当前点在边界，并且不是入口，就是出口
11            if (x, y) != (entrance[0], entrance[1]) and (x == 0 or x == m - 1 or y == 0 or y == n - 1):
12                return steps
13            for dx, dy in directions:
14                nx, ny = x + dx, y + dy
15                if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == ".":
16                    maze[nx][ny] = "+"
17                    q.append((nx, ny, steps + 1))
18        return -1