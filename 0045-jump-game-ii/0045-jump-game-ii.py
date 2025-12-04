class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        step=0
        max_pos=0
        cur_end=0
        for i in range(n-1):
            max_pos= max(nums[i]+i, max_pos)
            if i==cur_end:
                step+=1
                cur_end=max_pos
                if cur_end >= n - 1:
                    break  # 已经覆盖到最后，结束循环
        return step