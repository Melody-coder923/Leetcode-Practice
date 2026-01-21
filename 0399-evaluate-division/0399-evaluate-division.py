from collections import defaultdict
from typing import List, Set 

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def buildGraph(equations, values):
            graph = defaultdict(dict)
            for i, (a, b) in enumerate(equations):
                weight = values[i]
                graph[a][b] = weight
                graph[b][a] = 1.0 / weight
            return graph
        
        def dfs(graph, start, end, visited):
            if start not in graph:
                return -1.0
            if start == end:
                return 1.0
            visited.add(start)
            for neighbor, weight in graph[start].items():
                if neighbor not in visited:
                    result = dfs(graph, neighbor, end, visited)
                    if result != -1.0:
                        return weight * result
            return -1.0
        
        graph = buildGraph(equations, values)
        
        results = []
        for start, end in queries:
            if start not in graph or end not in graph:
                results.append(-1.0)
            else:
                visited = set()
                result = dfs(graph, start, end, visited)
                results.append(result)
        
        return results
    