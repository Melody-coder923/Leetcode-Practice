1class Solution:
2    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
3        m,n=len(nums1),len(nums2)
4        if m>n:
5            nums1, nums2 = nums2, nums1
6            m,n=n,m
7        
8        if m==0 and n==0:
9            return 0.0
10
11        l,r=0,m 
12        while l<=r:
13            i= (l+r)//2
14            j= (m+n+1)//2-i
15
16            maxleft1= float("-inf") if i==0 else nums1[i-1]
17            maxleft2= float("-inf") if j==0 else nums2[j-1]
18            minright1= float("inf") if i==m else nums1[i]
19            minright2= float("inf") if j==n else nums2[j]
20
21            if maxleft1<=minright2 and maxleft2<=minright1:
22                #奇数个
23                if (m+n)%2==1:
24                    return max(maxleft1,maxleft2)
25                #偶数个
26                else:
27                    return (max(maxleft1,maxleft2) + min(minright1, minright2))/2
28
29            elif maxleft1>minright2:
30                r=i-1
31            else:
32                l=i+1
33        return 0.0
34
35    
36        
37        
38        
39        
40        
41        
42        
43        
44        
45        
46        
47        
48        
49        
50        
51        
52        
53        
54        
55        
56        
57        
58        
59        
60        
61        
62        
63        if m>n:
64            nums1,nums2=nums2,nums1
65            m,n=n,m
66        if m==0 and n==0:
67            return 0.0  
68        
69        l,r=0,m  #切分位置，不是下标
70        while l<=r:
71            i=(l+r)//2
72            j= (m+n+1)//2-i 
73
74            maxleft1 = float("-inf") if i == 0 else nums1[i-1]
75            maxleft2 = float("-inf") if j == 0 else nums2[j-1]
76            minright1 = float("inf")  if i == m else nums1[i]
77            minright2 = float("inf")  if j == n else nums2[j]
78
79            if maxleft1 <= minright2 and maxleft2 <= minright1:
80                if (m + n) % 2 == 1:
81                    return max(maxleft1, maxleft2)
82                else:
83                    return (max(maxleft1, maxleft2) + min(minright1, minright2)) / 2
84                
85            elif maxleft1 > minright2:
86                r=i-1
87            else:
88                l=i+1
89        return 0.0
90
91