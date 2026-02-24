1class Solution:
2    def twoSum(self, numbers: List[int], target: int) -> List[int]:
3        left,right=0,len(numbers)-1
4        while left<right:
5            s=numbers[left]+numbers[right]
6            if s==target:
7                return [left+1,right+1]
8            elif s<target:
9                left+=1
10            else:
11                right-=1
12        
13        
14
15