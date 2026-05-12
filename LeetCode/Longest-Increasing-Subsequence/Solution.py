1class Solution:
2    def lengthOfLIS(self, nums: List[int]) -> int: 
3        sublist=[]     
4        for num in nums:
5            left,right=0,len(sublist)-1
6            while left<=right:
7                mid=left+(right-left)//2
8                if sublist[mid]<num:
9                    left=mid+1
10                else:
11                    right=mid-1
12            if left==len(sublist):
13               sublist.append(num)
14            else:
15                sublist[left]=num
16        
17        return len(sublist)
18            