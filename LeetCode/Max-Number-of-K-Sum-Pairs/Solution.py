1class Solution:
2    def maxOperations(self, nums: List[int], k: int) -> int:
3        count=defaultdict(int)
4        ans=0
5        for x in nums:
6            need=k-x
7            if count[need]>0:
8                ans+=1
9                count[need]-=1
10            else:
11                count[x]+=1
12        return ans