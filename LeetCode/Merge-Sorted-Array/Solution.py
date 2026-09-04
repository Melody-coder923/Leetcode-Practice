1class Solution:
2    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
3        """
4        Do not return anything, modify nums1 in-place instead.
5        """
6        length=len(nums1)
7        p=length-1
8        p1=m-1
9        p2=n-1
10        while p1>=0 and p2>=0:
11            if nums1[p1]>nums2[p2]:
12                nums1[p]=nums1[p1]
13                p1-=1
14            else:
15                nums1[p]=nums2[p2]
16                p2-=1
17            
18            p-=1
19        
20        while p2>=0:
21            nums1[p]=nums2[p2]
22            p-=1
23            p2-=1
24        
25
26