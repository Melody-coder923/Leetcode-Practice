class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # total >= target
        # not exist : return 0
        # positive -> sliding window
        n=len(nums)
        l=0
        minLen=float("inf")
        total=0
        for r in range(n):
            #sliding window while total >= target: 更新left指针
            total+=nums[r]
            if nums[r]==target:
                return 1
            while total>=target:
                minLen=min(minLen,r-l+1)
                total-=nums[l]
                l+=1
        return minLen if minLen!=float("inf") else 0
