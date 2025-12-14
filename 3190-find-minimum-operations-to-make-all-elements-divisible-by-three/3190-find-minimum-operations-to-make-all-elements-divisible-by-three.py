class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res=0
        for num in nums:
            mod=num%3
            if mod!=0:
                res+=1
        return res
