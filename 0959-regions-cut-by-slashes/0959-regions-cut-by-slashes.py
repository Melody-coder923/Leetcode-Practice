class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        parent = [i for i in range(4 * n * n)]
        #并差集
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            parent[find(x)] = find(y)

        #二维转一维,用base做合并
        for i in range(n):
            for j in range(n):
                base = 4 * (i * n + j)
                ch = grid[i][j]

                # 同一格内部连边
                if ch == ' ':
                    union(base + 0, base + 1)
                    union(base + 1, base + 2)
                    union(base + 2, base + 3)
                elif ch == '/':
                    union(base + 0, base + 3)
                    union(base + 1, base + 2)
                elif ch == '\\':
                    union(base + 0, base + 1)
                    union(base + 2, base + 3)
                 # 与邻格连边
                if i + 1 < n:  # 下方
                    union(base + 2, (base + 4 * n) + 0)
                if j + 1 < n:  # 右方
                    union(base + 1, (base + 4) + 3)
        return sum(find(i) == i for i in range(4 * n * n))