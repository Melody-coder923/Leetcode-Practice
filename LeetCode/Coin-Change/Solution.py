1class Solution:
2    def coinChange(self, coins: List[int], amount: int) -> int:
3        #memo
4        count=0
5        @lru_cache(None)
6        #def dfs
7        def dfs(remain):
8            #base case
9            if remain==0:
10                return 0
11            if remain<0:
12                return float("inf")
13            res=float("inf")
14            # break down
15            for coin in coins:
16                res=min(res,dfs(remain-coin)+1)
17            return res
18        res= dfs(amount) 
19        return res if res!=float("inf") else -1