1class Solution:
2    def nextPermutation(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        #1. 从右边找第一个下降点  12354，就是3
7        n=len(nums)
8        if n <= 1:
9            return
10        i=n-2
11        while i>=0 and nums[i]>=nums[i+1]:
12            i-=1
13
14        if i < 0:
15            nums.reverse()
16            return
17        
18        #2. 找右侧第一个比nums[i]大的
19        j=n-1
20        while j>i and nums[j]<=nums[i]:
21            j-=1
22        nums[i],nums[j]=nums[j],nums[i]
23
24        #3.反转后面的数组
25        l,r=i+1,n-1
26        while l<r:
27            nums[l],nums[r]=nums[r],nums[l]
28            l+=1
29            r-=1
30        