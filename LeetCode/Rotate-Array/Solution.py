1class Solution:
2    def rotate(self, nums: List[int], k: int) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        def reverse(nums,left,right):
7            while left<right:
8                nums[left],nums[right]=nums[right],nums[left]
9                left+=1
10                right-=1
11            return nums
12        n=len(nums)
13        k=k%n
14        reverse(nums,0,n-1)
15        reverse(nums,0,k-1)
16        reverse(nums,k,n-1)
17        return nums