1class Solution:
2    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
3        m,n=len(nums1),len(nums2)
4        if m>n:
5            nums1,nums2=nums2,nums1
6            m,n=n,m
7        
8        l,r=0,m
9        while l<=r:
10            i=(l+r)//2
11            j=(m+n+1)//2-i
12
13            maxLeft1= float("-inf") if i==0 else nums1[i-1]
14            maxLeft2= float("-inf") if j==0 else nums2[j-1]
15            minRight1= float("inf") if i==m else nums1[i]
16            minRight2= float("inf") if j==n else nums2[j]
17
18            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
19                if (m+n)%2==1:
20                    return max(maxLeft1,maxLeft2)
21                else:
22                    return (max(maxLeft1,maxLeft2)+min(minRight1,minRight2))/2
23            elif maxLeft1>minRight2:
24                r=i-1
25            else:
26                l=i+1
27        return 0.0