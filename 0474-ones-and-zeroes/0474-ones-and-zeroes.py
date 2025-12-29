class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        #dp[i][j]是我们剩余i和j时候最多能装多少个物品
        dp=[ [0] *(n+1) for _ in range(m+1) ]
        for word in strs:
            zero=one=0
            for char in word:
                if char=="0":
                    zero+=1
                else:
                    one+=1
            for i in range(m,zero-1,-1):
                for j in range(n,one-1,-1):
                    dp[i][j]=max(dp[i][j],dp[i-zero][j-one]+1)
        return dp[m][n]
            