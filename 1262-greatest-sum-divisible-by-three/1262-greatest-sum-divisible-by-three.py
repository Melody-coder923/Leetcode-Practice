from typing import List

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # dp[i] 表示当前余 i 的最大和
        dp = [0, -10**9, -10**9]  # 用大负数代替 -inf

        for num in nums:
            tmp = dp[:]  # 拷贝旧状态
            for i in range(3):
                new_sum = tmp[i] + num
                new_rem = new_sum % 3       # 这里都是整数，不会报错
                dp[new_rem] = max(dp[new_rem], new_sum)

        return dp[0]
