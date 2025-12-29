class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #a+b=sum
        #a-b=target
        #a=(sum+target)//2
        total=sum(nums)
        if (total+target)%2!=0 or total<abs(target):
            return 0
        x= (total+target)//2
        n=len(nums)
        dp= [[0] * (x+1) for _ in range(n+1)]
        dp[0][0]=1
        for i in range(1,n+1):
            for j in range(x+1):
                dp[i][j]=dp[i-1][j]
                if j>=nums[i-1]:
                    dp[i][j]=dp[i-1][j]+dp[i-1][j-nums[i-1]]
        return dp[n][x]