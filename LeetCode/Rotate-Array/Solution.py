1class Solution:
2    def rotate(self, nums: List[int], k: int) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        n= len(nums)
7        k=k%n
8        self.reverse(nums,0,n-1)
9        self.reverse(nums,0,k-1)
10        self.reverse(nums,k,n-1)
11    def reverse(self,nums:List[int],left:int, right:int) -> None:
12        while left<right:
13            nums[left],nums[right]=nums[right],nums[left]
14            left+=1
15            right-=1
16        