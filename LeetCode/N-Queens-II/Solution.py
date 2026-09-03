1class Solution:
2    def totalNQueens(self, n: int) -> int:
3        cols= set()
4        diag=set() #row+col
5        reverse_diag=set() # col-row
6        count=0
7
8        def backtrack(row):
9            nonlocal count
10            if row==n:
11                count+=1
12                return 
13
14            for col in range(n):
15                if col in cols or row+col in diag or col-row in reverse_diag:
16                    continue
17                cols.add(col)
18                diag.add(row+col)
19                reverse_diag.add(col-row)
20                backtrack(row+1)
21                cols.remove(col)
22                diag.remove(row+col)
23                reverse_diag.remove(col-row)
24
25        backtrack(0)
26        return count
27    