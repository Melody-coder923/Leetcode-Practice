1class Solution:
2    def totalNQueens(self, n: int) -> int:
3        cols=set()
4        diag=set()
5        reverse_diag=set()
6        count=0
7
8        def backtrack(row):
9            nonlocal count
10            if row==n:
11                count+=1
12                return 
13            
14            for col in range(n):
15                if col in cols or col-row in reverse_diag or row+col in diag:
16                    continue
17                
18                cols.add(col)
19                diag.add(row+col)
20                reverse_diag.add(col-row)
21                backtrack(row+1)
22                cols.remove(col)
23                diag.remove(row+col)
24                reverse_diag.remove(col-row)
25            
26        backtrack(0)
27        return count
28            
29            