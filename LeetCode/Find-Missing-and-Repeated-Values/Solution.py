1class Solution:
2    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
3        # output: repeat and missing
4
5        # dict if appeear [repeat, ]
6        # n： how many numbers max= 
7        # [0,0,0,0,
8           
9        n=len(grid) 
10        lst=[0]* (n*n)
11        for i in range(n):
12            for j in range(n):
13                lst[grid[i][j]-1]+=1
14        
15        missing=lst.index(0)
16        repeat=lst.index(2)
17        return [repeat+1,missing+1]