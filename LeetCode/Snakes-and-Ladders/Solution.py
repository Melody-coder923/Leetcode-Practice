1from collections import deque
2
3class Solution:
4    def snakesAndLadders(self, board: List[List[int]]) -> int:
5        n = len(board)
6        target = n * n
7
8        # flatten board
9        flatten = []
10        left_to_right = True
11        for row in range(n - 1, -1, -1):
12            if left_to_right:
13                flatten.extend(board[row])
14            else:
15                flatten.extend(board[row][::-1])
16            left_to_right = not left_to_right
17
18        # BFS
19        q = deque([0])
20        visited = set([0])
21        step = 0
22
23        while q:
24            size = len(q)
25            for _ in range(size):
26                curr = q.popleft()
27                if curr == target - 1:
28                    return step
29
30                for nxt in range(curr + 1, min(curr + 6, target - 1) + 1):
31                    if flatten[nxt] != -1:
32                        dest = flatten[nxt] - 1
33                    else:
34                        dest = nxt
35
36                    if dest not in visited:
37                        visited.add(dest)
38                        q.append(dest)
39
40            step += 1
41
42        return -1
43