1class Solution:
2    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
3        """
4        Do not return anything, modify nums1 in-place instead.
5        """
6        i=m-1
7        j=n-1
8        p=len(nums1)-1
9        while i>=0 and j>=0:
10            if nums1[i]>nums2[j]:
11                nums1[p]=nums1[i]
12                i-=1
13            else:
14                nums1[p]=nums2[j]
15                j-=1
16            p-=1
17        while j>=0:
18            nums1[p]=nums2[j]
19            j-=1
20            p-=1