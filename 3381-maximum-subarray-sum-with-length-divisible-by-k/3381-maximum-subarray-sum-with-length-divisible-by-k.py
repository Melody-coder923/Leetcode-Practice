class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:

        """       
        (r + 1) % k == l % k,子数组和pre[r+1] - pre[l]
        把所有前缀下标按 index % k 分组,在同一组里做「最大差值」

        nums = [-5, 1, 2, -3, 4]
        k = 2
        index:   0   1   2   3   4   5
        pre:     0  -5  -4  -2  -5  -1
        index%2: 0   1   0   1   0   1
        mod = 0 组
        pre = [0, -4, -5]
        -4 - 0 = -4
        -5 - 0 = -5

        mod = 1 组
        pre = [-5, -2, -1]
        -2 - (-5) = 3
        -1 - (-5) = 4  ✅
        👉 这个 4 就是答案
        对应子数组：[1,2,-3,4]

        """
        n = len(nums)
        prefix = 0
        minPrefix = [float('inf')] * k
        minPrefix[0] = 0
        
        ans = float('-inf')

        for i in range(n):
            prefix += nums[i]
            mod = (i + 1) % k 

            ans = max(ans, prefix - minPrefix[mod])
            minPrefix[mod] = min(minPrefix[mod], prefix)
        return ans