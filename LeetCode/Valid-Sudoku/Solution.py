1class Solution:
2    def isValidSudoku(self, board: List[List[str]]) -> bool:
3        """
4        check if valid-> 3rules no repeatation
5        1. row set()
6        2.col set()
7        3. sub box  set()
8        dict row
9        dict col 
10        dict subbox
11        """
12        m=len(board)
13        rows=[set() for _ in range(m)]
14        cols=[set() for _ in range(m)]
15        sub_boxes=[set() for _ in range(m)]
16
17        for i in range(m):
18            for j in range(m):
19                if board[i][j]==".":
20                    continue
21                if board[i][j] in rows[i]:
22                    return False
23                if board[i][j] in cols[j]:
24                    return False
25                # 坐标到一个数字 
26                box_id = (i // 3) * 3 + (j // 3)
27                if board[i][j] in sub_boxes[box_id]:
28                    return False
29                
30                rows[i].add(board[i][j])
31                cols[j].add(board[i][j])
32                sub_boxes[box_id].add(board[i][j])
33        return True
34
35