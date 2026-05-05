1class Solution:
2    def nextPermutation(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        # scan from right to left to find the first nums[i]>=nums[i+1]
7        n=len(nums)
8        if n <= 1:
9            return
10        i=n-2
11        while i>=0 and nums[i]>=nums[i+1]:
12            i-=1
13        # i will stop at the nums[i]> nums[i+1]     1 2 3 5 4      1 2  4 3 4
14        if i < 0:  # 全递减，如 3 2 1
15            nums.reverse()
16            return
17        
18        # find the first bigger number from right
19        j=n-1
20        while nums[j]<=nums[i]:
21            j-=1
22        nums[i],nums[j]=nums[j],nums[i]
23        
24        left,right=i+1,n-1
25        while left<right:
26            nums[left], nums[right] = nums[right], nums[left]
27            left += 1
28            right -= 1