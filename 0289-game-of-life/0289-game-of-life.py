class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Input : live 1 , dead 0
        # Constraint: 1. neigh live<2, live->die  2. neigh live 2 or 3 live, live-> live
        #3. neigh live>3,live-> die  4.  neigh live>3, die->live
        # helper-> die or live
        m,n=len(board),len(board[0])
        # follow the rules to check every cell's neigh
        directions=[(0,1),(0,-1),(1,0),(-1,0),(-1,1),(1,1),(1,-1),(-1,-1)]
    
        def live_neighbors(x, y):
            count = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    # 原来活或者标记为活→死都算原来活
                    if board[nx][ny] in (1, 2):
                        count += 1
            return count
    
        # iterate all cell and then check by helper
        for i in range(m):
            for j in range(n):
                count = live_neighbors(i, j)
                if board[i][j] == 1:
                    if count < 2 or count > 3:
                        board[i][j] = 2  # 活→死
                else:  # board[i][j] == 0
                    if count == 3:
                        board[i][j] = 3  # 死→活
        # 第二次遍历：恢复 0/1
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1