class Solution:
    def jump(self, nums: list[int]) -> int:
        n=len(nums)
        step=0
        farest=0
        end=0
        if n==1:
            return 0
        for i,num in enumerate(nums):
            farest=max(farest,num+i)

            if i==end:
                step+=1
                end=farest

                if farest>=n-1:
                    return step

        return step
