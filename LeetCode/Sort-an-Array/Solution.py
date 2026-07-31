1class Solution:
2    def sortArray(self, nums: List[int]) -> List[int]:
3        def merge(left,right):
4            m,n=len(left),len(right)
5            i=j=0
6            res=[]
7            while i<m and j<n:
8                if left[i]<=right[j]:
9                    res.append(left[i])
10                    i+=1
11                else:
12                    res.append(right[j])
13                    j+=1
14
15            res.extend(left[i:])
16            res.extend(right[j:])
17
18            return res
19        
20        def split(arr):
21            if len(arr) <= 1:
22                return arr
23            mid = len(arr) // 2
24            left=split(arr[mid:])
25            right=split(arr[:mid])
26
27            return merge(left,right)
28
29        return split(nums)
30
31
32