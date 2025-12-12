from typing import List

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, 0, 0]  # 初始状态，全用整数即可

        for num in nums:
            a, b, c = dp[:]  # 拷贝旧状态
            dp[(a + num) % 3] = max(dp[(a + num) % 3], a + num)
            dp[(b + num) % 3] = max(dp[(b + num) % 3], b + num)
            dp[(c + num) % 3] = max(dp[(c + num) % 3], c + num)

        return dp[0]