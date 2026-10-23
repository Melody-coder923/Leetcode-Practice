class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return 0
        step=farthest=end=0
        for i,num in enumerate(nums):
            farthest=max(farthest,num+i)
            if i==end:
                step+=1
                end=farthest
                if farthest>=n-1:
                    return step
        return step
