1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        count=Counter(nums)
4        for key in count:
5            if count[key]>=2:
6                return True
7        
8        return False