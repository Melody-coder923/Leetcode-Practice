1class Solution:
2    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
3        m,n=len(nums1),len(nums2)
4        if m>n:
5            nums1,nums2=nums2,nums1
6            m,n=n,m
7
8        l,r=0,m
9        while l<=r:
10            i=(l+r)//2 #左边所有的都能取到，算的不只是下标,是切分位置
11            j=(m+n+1)//2-i #故意让左边多1个
12
13            maxLeft1= float("-inf") if i==0 else nums1[i-1]
14            maxLeft2= float("-inf") if j==0 else nums2[j-1]
15
16            minRight1= float("inf") if i==m else nums1[i]
17            minRight2= float("inf") if j==n else nums2[j]
18
19            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
20                if (m+n)%2==1:
21                    return max(maxLeft1,maxLeft2)
22                else:
23                    return (max(maxLeft1,maxLeft2)+min(minRight1,minRight2))/2
24
25            elif maxLeft1>minRight2:
26                r=i-1
27
28            else:
29                l=i+1
30
31        return 0.0
32    
33
34    