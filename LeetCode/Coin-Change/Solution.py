1class Solution:
2    def coinChange(self, coins: List[int], amount: int) -> int:
3        m=len(coins)
4
5        @lru_cache(None)
6        def dfs(target):
7            nonlocal res
8            if target==0:
9                return 0
10            if target<0:
11                return float("inf")
12            res= float("inf")
13            #break down
14            for coin in coins:
15                res=min(res,dfs(target-coin)+1)
16
17            return res
18        res=dfs(amount)
19        return res if res!=float("inf") else -1
20
21    """
22            amounts
23              0  1. 2  3  4  5 6 7 8 9 10 11
24    coins 0   0. e  e. e  e. e e e e e e   e
25          1   0  
26          2   0
27          5   0
28
29    """
30