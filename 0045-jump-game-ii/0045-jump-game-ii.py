class Solution:
    def jump(self, nums: List[int]) -> int:
        cur_end = 0        # 当前跳跃的边界
        farthest = 0       # 当前区间能跳到的最远距离
        steps = 0

        for i in range(len(nums) - 1):
            # 在当前区间内不断扩展下一跳能达到的最远范围
            farthest = max(farthest, i + nums[i])

            # 到达当前跳跃的边界 → 必须跳一步
            if i == cur_end:
                steps += 1
                cur_end = farthest   # 更新下一跳的区间

        return steps