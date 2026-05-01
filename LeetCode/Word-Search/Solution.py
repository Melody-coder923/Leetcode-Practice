1class Solution:
2    def exist(self, board: List[List[str]], word: str) -> bool:
3        if not board or not board[0] or not word:
4            return False
5        m, n = len(board), len(board[0])
6        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
7
8        def dfs(x, y, index):
9            if index == len(word):
10                return True
11            if (x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or
12        board[x][y] != word[index] or board[x][y] == '#'):
13                return False
14            temp = board[x][y]
15            board[x][y] = '#'
16            directions = [(-1,0), (1,0), (0,-1), (0,1)]
17            for dx, dy in directions:
18                if dfs(x + dx, y + dy, index + 1):
19                    return True
20            board[x][y] = temp
21            return False
22
23        for i in range(len(board)):
24            for j in range(len(board[0])):
25                if board[i][j] == word[0]:  # 找到首字母
26                    if dfs(i, j, 0):  # 从这里开始DFS
27                        return True
28        return False