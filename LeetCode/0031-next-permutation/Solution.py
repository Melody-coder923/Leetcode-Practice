class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        if n<=1:
            return 
        i=n-2
        # 从右往左找下降点
        while i>=0 and nums[i]>=nums[i+1]:
            i-=1
        if i<0:
            nums.reverse()
            return
        #找右边第一个比 nums[i] 大的数
        j=n-1
        while j>=i and nums[i]>=nums[j]:
            j-=1
        nums[i],nums[j]=nums[j],nums[i]

        l,r=i+1,n-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1