1class Solution:
2    def rotate(self, nums: List[int], k: int) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        n=len(nums)
7        k=k%n
8
9        def reverse(l,r,nums):
10            while l<r:
11                nums[l],nums[r]=nums[r],nums[l]
12                l+=1
13                r-=1
14        
15        reverse(0,n-1,nums)
16        reverse(0,k-1,nums)
17        reverse(k,n-1,nums)
18        
19      