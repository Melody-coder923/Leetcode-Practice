1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        dict={}
4        for i,num in enumerate(nums):
5            if target-num in dict:
6                return [dict[target-num],i]
7            dict[num]=i
8        return -1