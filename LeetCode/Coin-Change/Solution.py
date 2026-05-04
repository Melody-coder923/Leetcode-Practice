1class Solution:
2    from collections import deque
3    def coinChange(self, coins: List[int], amount: int) -> int:
4        q=deque([0])
5        level=0
6        visited={0}
7        while q:
8            for _ in range(len(q)):
9                curr=q.popleft()
10                if curr ==amount:
11                    return level
12                for coin in coins:
13                    nxt=curr+coin
14                    if nxt not in visited and nxt<=amount:
15                        q.append(nxt)
16                        visited.add(nxt)
17            level+=1
18        return -1