class Solution:

    
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        """
            Input: bottom left-> [curr + 1, min(curr + 6, n2)] 6 sides die roll 
            1. snake and ladder: board[r][c]!=-1 to board[r][c]
            2. destination : n**2

            Output: least number of dice rolls to destination

        """
        
        def flatten_board(board):
            n = len(board)
            flat = []
            for r in range(n-1, -1, -1):
                row = board[r] if (n-1-r) % 2 == 0 else board[r][::-1]
                flat.extend(row)
            return flat  # flat[0] 对应 label 1, flat[n*n-1] 对应 label n^2
        n = len(board)
        flat = flatten_board(board)
        
        target = n * n
        visited = set()
        queue = deque()
        queue.append((1, 0))  # (当前格子, 已掷骰子次数)
        visited.add(1)
        
        while queue:
            pos, moves = queue.popleft()
            if pos == target:
                return moves
            
            for step in range(1, 7):  # 掷骰子 1~6
                next_pos = pos + step
                if next_pos > target:
                    continue
                # 看是否有梯子或蛇
                if flat[next_pos - 1] != -1:
                    next_pos = flat[next_pos - 1]
                
                if next_pos not in visited:
                    visited.add(next_pos)
                    queue.append((next_pos, moves + 1))
        
        return -1  # 无法到达