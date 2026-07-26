1class Solution:
2    def nextPermutation(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        n=len(nums)
7        if n<=1:
8            return 
9        i=n-2
10        # 从右往左找下降点
11        while i>=0 and nums[i]>=nums[i+1]:
12            i-=1
13        if i<0:
14            nums.reverse()
15            return
16        #找右边第一个比这个数小的
17        j=n-1
18        while j>=i and nums[i]>=nums[j]:
19            j-=1
20        nums[i],nums[j]=nums[j],nums[i]
21
22        l,r=i+1,n-1
23        while l<r:
24            nums[l],nums[r]=nums[r],nums[l]
25            l+=1
26            r-=1