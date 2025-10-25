class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        #鸡蛋怕碎不能用二分, 本质上是“在有限资源下，找最少测试次数”的优化问题 
        #用 k 个鸡蛋，做 m 次尝试，最多可以测试的楼层数
        #当我们在某层楼扔鸡蛋时，有两种可能：鸡蛋碎了 → 我们还剩 k-1 个鸡蛋，尝试次数 -1；鸡蛋没碎 → 鸡蛋数量不变，尝试次数 -1。
        #dp[k][m]=dp[k-1][m-1]+dp[k][m-1]+1 二维转为一维 原二维 dp[k][m] 的状态转移只依赖于 前一行（k-1）和 前一列（m-1）需要反向更新不会覆盖
        dp=[0]*(k+1)
        m = 0
        while dp[k] < n:
            m += 1
            for i in range(k, 0, -1):
                dp[i] = dp[i] + dp[i-1] + 1
        return m

