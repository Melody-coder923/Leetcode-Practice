1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        p1=[]
4        p2=[]
5        res=[]
6        prev=1
7        for i in nums:
8            p1.append(prev)
9            prev*=i
10        prev=1
11        for j in nums[::-1]:
12            p2.append(prev)
13            prev*=j
14        p2.reverse()
15        for i in range(len(nums)):
16            res.append(p1[i]*p2[i])
17       
18        
19        return res