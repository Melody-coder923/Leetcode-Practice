class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        #超出k个0 l移动直到满足要求
        l=0
        res=0
        count=0
        for r,num in enumerate(nums):
            if num==0:
                count+=1
            while count>k:
                if nums[l]==0:
                    count-=1
                l+=1
            res=max(res,r-l+1)
        return res