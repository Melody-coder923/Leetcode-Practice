1class Solution:
2    def isValidSudoku(self, board: List[List[str]]) -> bool:
3        rows = [set() for _ in range(9)]
4        cols = [set() for _ in range(9)]
5        boxes = [set() for _ in range(9)]  # 3x3 宫格编号：0~8
6
7        for i in range(9):
8            for j in range(9):
9                val = board[i][j]
10                if val == ".":
11                    continue
12
13                if val in rows[i]:
14                    return False
15                rows[i].add(val)
16
17                if val in cols[j]:
18                    return False
19                cols[j].add(val)
20
21                box_index = (i // 3) * 3 + (j // 3)
22                if val in boxes[box_index]:
23                    return False
24                boxes[box_index].add(val)
25
26        return True
27