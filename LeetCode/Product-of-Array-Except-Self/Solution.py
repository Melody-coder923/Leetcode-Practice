1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        """
4        left->right preproduct
5        1  1   2   6
6        right->left preproduct
7        24  12   4  1
8
9        24   12. 8 6
10        """
11        n=len(nums)
12        res=[]
13        prefix=1
14        for num in nums:
15            res.append(prefix)
16            prefix=prefix*num
17            
18
19        suffix=1
20        for i in range(n-1,-1,-1):
21            res[i]=res[i]*suffix
22            suffix=suffix*nums[i]
23
24        return res
25
26      