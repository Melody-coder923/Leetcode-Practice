1class Solution:
2    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
3        m,n=len(nums1),len(nums2)
4        if m>n:
5            nums1,nums2=nums2,nums1
6            m,n=n,m
7        if m==0 and n==0:
8            return 0.0  
9        
10        l,r=0,m  #切分位置，不是下标
11        while l<=r:
12            i=(l+r)//2
13            j= (m+n+1)//2-i 
14
15            maxleft1 = float("-inf") if i == 0 else nums1[i-1]
16            maxleft2 = float("-inf") if j == 0 else nums2[j-1]
17            minright1 = float("inf")  if i == m else nums1[i]
18            minright2 = float("inf")  if j == n else nums2[j]
19
20            if maxleft1 <= minright2 and maxleft2 <= minright1:
21                if (m + n) % 2 == 1:
22                    return max(maxleft1, maxleft2)
23                else:
24                    return (max(maxleft1, maxleft2) + min(minright1, minright2)) / 2
25                
26            elif maxleft1 > minright2:
27                r=i-1
28            else:
29                l=i+1
30        return 0.0
31
32