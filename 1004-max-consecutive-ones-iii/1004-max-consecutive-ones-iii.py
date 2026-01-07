class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res=0
        l=0
        change=0
        for r,num in enumerate(nums):
            if num==0: 
                change+=1
            while change>k:
                if nums[l]==0:
                    change-=1
                l+=1
            res=max(res,r-l+1)
        return res
                
            

                
                
                