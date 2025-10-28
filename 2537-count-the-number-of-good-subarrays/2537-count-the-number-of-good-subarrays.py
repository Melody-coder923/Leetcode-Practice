class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        # 滑动窗口: 统计频率//2>0的对数 
        count = defaultdict(int)   # 统计每个数在窗口中的出现次数
        pairs = 0                  # 当前窗口中“相等数对”的数量
        res = 0                    # 答案
        l = 0                      # 左指针

        for r, x in enumerate(nums):  # 右指针从0到n-1依次扩张窗口
            # 加入新元素 x 时，它与之前相同的 count[x] 个元素形成新 pairs
            pairs += count[x]
            count[x] += 1

            # 如果当前窗口内的相等对数 ≥ k，尝试移动左边界 l，压缩窗口
            # 移除 nums[l] 会减少 (count[nums[l]] - 1) 个相等对
            while pairs - (count[nums[l]] - 1) >= k:
                pairs -= (count[nums[l]] - 1)
                count[nums[l]] -= 1
                l += 1

            # 当 pairs ≥ k 时，以 r 结尾的所有子数组 [0..l-1, r] 都合法
            # 所以增加 l 个
            if pairs >= k:
                res += l+1

        return res