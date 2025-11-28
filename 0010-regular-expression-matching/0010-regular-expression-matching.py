class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #Step1:创建dp列表
        n,m=len(s),len(p)
        dp=[[False]*(m+1) for _ in range(n+1)]
        #Step2:初始化包括两部分: dp[0][0] ; 以及特殊情况:dp[0][j]情况 如果 p[j-1] 是 '*'，可以跳过前两个字符
        dp[0][0]=True

        # 初始化 dp[0][j] (空串 vs 模式)
        for j in range(2,m+1):
            if p[j-1]=="*":
                dp[0][j] = dp[0][j-2]  # '*' 可以匹配 0 个前面字符

        #Step3: dp填充
        for i in range(1,n+1):
            for j in range(1,m+1):
        # 情况1: 当前模式不是 '*' (普通字符或者 '.')
                if p[j-1]!= "*":
                    # match 当前字符吗？s[i-1] == p[j-1] or p[j-1] == '.'
                    if p[j-1] == s[i-1] or p[j-1] == '.':
                        dp[i][j]=dp[i-1][j-1]
        # 情况2: 当前模式是 '*'  
                else:
                    # 星号情况1: 代表0个
                    dp[i][j] = dp[i][j-2]  # '*' 和前面字符当作整体跳过
                    # 星号情况2: 代表1个或多个
                    # 先判断能否匹配当前字符
                    if p[j-2] == s[i-1] or p[j-2] == '.':
                        # 如果匹配, 用 '*' 吃掉 s[i-1], 继续看前面的状态 dp[i-1][j]
                        dp[i][j] = dp[i][j] or dp[i-1][j]
        return dp[n][m]