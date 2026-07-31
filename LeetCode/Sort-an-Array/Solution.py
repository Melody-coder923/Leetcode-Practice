1class Solution:
2    def sortArray(self, nums: List[int]) -> List[int]:
3        #归并排序 -linkedlist arr1 arr2- merge
4
5        def merge(l1,l2):
6            m,n=len(l1),len(l2)
7            i,j=0,0
8            res=[]
9            while i <m and j<n:
10                if l1[i]<=l2[j]:
11                    res.append(l1[i])
12                    i+=1
13                else:
14                    res.append(l2[j])
15                    j+=1
16
17            res.extend(l1[i:])
18            res.extend(l2[j:])
19            return res
20        
21        def merge_sort(arr):
22            #base case
23            if len(arr)<=1:
24                return arr
25            mid=len(arr)//2
26            left=merge_sort(arr[:mid])
27            right=merge_sort(arr[mid:])
28            return merge(left,right)
29           
30        return merge_sort(nums)