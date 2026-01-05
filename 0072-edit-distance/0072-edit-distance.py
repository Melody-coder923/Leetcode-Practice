class Solution:
    #定义 dp[i][j] 为 word1 的前 i 个字符转换成 word2 的前 j 个字符所需的最少操作数。
    def minDistance(self, word1: str, word2: str) -> int:
        m,n=len(word1),len(word2)
        if m==0:
            return n
        if n==0:
            return m
        dp= [ [0]*(n+1) for _ in range(m+1) ]
        #base case
        for i in range(m+1):
            dp[i][0]=i
        for j in range(n+1):
            dp[0][j]=j
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
        return dp[m][n]
                