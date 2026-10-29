class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        @lru_cache(None)
        def dfs(i):
            if i<0:
                return 1
            res=0
            if s[i]!="0":
                res+=dfs(i-1)

            if i-1>=0 and 10<=int(s[i-1:i+1])<=26:
                res+=dfs(i-2)
            return res
        
        return dfs(n-1)