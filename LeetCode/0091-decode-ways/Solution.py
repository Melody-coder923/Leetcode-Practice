class Solution:
    def numDecodings(self, s: str) -> int:
        #edge case
        n=len(s)
        if n==1 and s[0]!="0":
            return 1
        if s[0]=="0":
            return 0
        
        @lru_cache(None)
        def dfs(i):
            #base case
            if i<0:
                return 1
            res=0
            #single
            if s[i]!="0":
                res+=dfs(i-1)
            
            #double
            if i-1>=0 and 10<=int(s[i-1:i+1])<=26:
                res+=dfs(i-2)
            
            return res
        
        return dfs(n-1)