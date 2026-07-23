1class Solution:
2    def threeSumClosest(self, nums: List[int], target: int) -> int:
3        nums.sort()
4        closest = float('inf')
5        for i in range(len(nums)):
6            left=i+1
7            right=len(nums)-1
8            while left<right:
9                total=nums[left]+nums[right]+nums[i]
10                if abs(total - target) < abs(closest - target):
11                    closest = total
12                if total<target:
13                    left+=1
14                elif total > target:
15                    right -= 1
16                else:
17                    return target
18        return closest