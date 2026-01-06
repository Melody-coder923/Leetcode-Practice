class Solution:
    def jump(self, nums: List[int]) -> int:
        """
            end        ：当前这一步能到的最远边界
            farthest  ：在当前区间内，下一步能到的最远位置
            steps     ：已经用了多少步
        """
        n = len(nums)
        steps = 0
        end = 0
        farthest = 0

        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if i == end:
                steps += 1
                end = farthest

        return steps