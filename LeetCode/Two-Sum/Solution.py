1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        map=defaultdict(int)
4        for idx,num in enumerate(nums):
5            if target-num in map:
6                return [idx,map[target-num]]
7            map[num]=idx
8        return -1