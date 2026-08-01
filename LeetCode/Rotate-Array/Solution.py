1class Solution:
2    def rotate(self, nums: List[int], k: int) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        #取余数，避免重复
7        n=len(nums)
8        k%=n
9        start=0
10        count=0
11
12        while count<n:
13            cur=start
14            prev = nums[start]
15            
16            while True:
17                nxt= (cur+k)%n
18                nums[nxt], prev = prev, nums[nxt]
19                cur=nxt
20                count+=1
21                if cur==start:
22                    break
23            start+=1
24
25