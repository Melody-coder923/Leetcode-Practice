1class Solution:
2    def coinChange(self, coins: List[int], amount: int) -> int:
3        m=len(coins)
4
5        @lru_cache(None)
6        def dfs(target):
7            if target==0:
8                return 0
9            if target<0:
10                return float("inf")
11            res= float("inf")
12            #break down
13            for coin in coins:
14                res=min(res,dfs(target-coin)+1)
15
16            return res
17        res=dfs(amount)
18        return res if res!=float("inf") else -1
19
20    """
21            amounts
22              0  1. 2  3  4  5 6 7 8 9 10 11
23    coins 0   0. e  e. e  e. e e e e e e   e
24          1   0  
25          2   0
26          5   0
27
28    """
29