class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # s1+s2=sum
        # s1-s2=diff
        # 2s1=sum+diff
        #  diff= 2s1-sum  我们希望s1尽量等于sum/2
        target=sum(stones)//2
        m= len(stones)
        dp= [[0] * (target+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,target+1):
                dp[i][j]=dp[i-1][j]
                if j>=stones[i-1]:
                    dp[i][j]=max(stones[i-1]+dp[i-1][j-stones[i-1]], dp[i][j])
        return sum(stones)-2*dp[m][target]   