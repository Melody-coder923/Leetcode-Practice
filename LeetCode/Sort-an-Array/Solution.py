1class Solution:
2    def sortArray(self, nums: List[int]) -> List[int]:
3        if len(nums)<=1:
4             return nums
5        num=len(nums)//2
6        left=self.sortArray(nums[:num])
7        right=self.sortArray(nums[num:])
8        return self.merge(left,right)
9    def merge(self,left,right):
10        l,r=0,0
11        result=[]
12        while l<len(left) and r<len(right):
13            if left[l]<right[r]:
14                result.append(left[l])
15                l+=1
16            else:
17                result.append(right[r])
18                r+=1
19        result+= left[l: ]
20        result+= right[r:]
21        return result           