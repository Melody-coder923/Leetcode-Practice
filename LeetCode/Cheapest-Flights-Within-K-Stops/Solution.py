1class Solution:
2    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
3        check= [float("inf")]*n
4        check[src]=0
5
6        for i in range(k+1):
7            temp=check[:]
8            for start,end,w in flights:
9                if check[start] != float("inf") and check[start]+w<temp[end]:
10                    temp[end] = check[start] + w
11            check=temp
12        return -1 if check[dst] == float("inf") else check[dst]