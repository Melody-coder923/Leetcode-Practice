class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        2, 3, 1, 1, 4
        0  1  2  3  4
        c     c
              end

        1. end: 第一范围    step 
        2. 超过end范围,属于下个范围, 更换end=farest, step+1
        3. farest: 范围内最远跳的位置 下次end
        """

        end=0
        farest=0
        n=len(nums)
        steps=0
        for i in range(n-1):
            farest=max(farest,nums[i]+i)
            if farest>=n-1:
                return steps+1
            if i==end:
                steps+=1
                end=farest
        return steps