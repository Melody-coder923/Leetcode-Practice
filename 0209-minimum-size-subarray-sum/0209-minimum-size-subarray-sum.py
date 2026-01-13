class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        total=0
        minLen = float("inf")
        for r in range(len(nums)):
            total+=nums[r]               
            while total>=target:
                minLen=min(r-l+1,minLen)
                total-=nums[l]
                l+=1

        return minLen if minLen!=float("inf") else 0

        