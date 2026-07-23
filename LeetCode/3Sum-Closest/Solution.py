1class Solution:
2    def threeSumClosest(self, nums: List[int], target: int) -> int:
3        nums.sort()
4        n=len(nums)
5        closest=float("inf")
6        for i in range(n):
7            l,r=i+1,n-1
8            while l<r:
9                total=nums[i]+nums[l]+nums[r]
10                if abs(total-target)<abs(target-closest):
11                    closest=total
12                
13                if total>target:
14                    r-=1
15                elif total<target:
16                    l+=1
17                else:
18                    return total
19            
20        return closest