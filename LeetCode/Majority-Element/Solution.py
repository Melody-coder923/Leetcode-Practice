1class Solution:
2    def majorityElement(self, nums: List[int]) -> int:
3        n=len(nums)
4        if n==1:
5            return nums[0]
6        
7        win=nums[0]
8        count=1
9        for num in nums[1:]:
10            if num==win:
11                count+=1
12            else:
13                count-=1
14                if count==0:
15                    win=num
16                    count=1
17        
18        return win
19