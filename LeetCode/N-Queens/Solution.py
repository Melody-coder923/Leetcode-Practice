1class Solution:
2    def solveNQueens(self, n: int) -> List[List[str]]:
3        result = []
4        board = ['.' * n for _ in range(n)] 
5        def backtrack(row):
6            if row == n:
7                result.append(board[:])
8                return
9            for col in range(n):
10                if is_valid(board, row, col):
11                    board[row] = board[row][:col] + 'Q' + board[row][col+1:]
12                    backtrack(row + 1)
13                    board[row] = board[row][:col] + '.' + board[row][col+1:]
14        def is_valid(board, row, col):
15            for i in range(row):
16                if board[i][col] == 'Q':
17                    return False
18            i, j = row - 1, col - 1
19            while i >= 0 and j >= 0:
20                if board[i][j] == 'Q':
21                    return False
22                i -= 1
23                j -= 1
24            i, j = row - 1, col + 1
25            while i >= 0 and j < n:
26                if board[i][j] == 'Q':
27                    return False
28                i -= 1
29                j += 1
30            return True
31        backtrack(0)
32        return result