1class Solution:
2    def twoSum(self, numbers: List[int], target: int) -> List[int]:
3        n=len(numbers)
4        l,r=0,n-1
5        while l<r:
6            total=numbers[l]+numbers[r]
7            if total==target:
8                return [l+1,r+1]
9            elif total>target:
10                r-=1
11            else:
12                l+=1
13        