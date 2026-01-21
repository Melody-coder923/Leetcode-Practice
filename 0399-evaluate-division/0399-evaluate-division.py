from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # build graph to show their realationship a/b   b/a
        graph = defaultdict(dict)

        for (x, y), val in zip(equations, values):
            graph[x][y] = val       # a -> b = 2
            graph[y][x] = 1 / val

        # dfs to caculate weight
        def dfs(start, end, visited):
            if start not in graph:
                return -1.0
            if start == end:
                return 1.0
            visited.add(start)
            
            for neighbor, value in graph[start].items():
                if neighbor in visited:
                    continue
                res= dfs(neighbor, end, visited)
                if res!= -1.0:
                    return value * res  # 累乘
            return -1.0

        # collect res
        res=[]
        for x,y in queries:
            visited=set()
            res.append(dfs(x,y,visited))
        return res