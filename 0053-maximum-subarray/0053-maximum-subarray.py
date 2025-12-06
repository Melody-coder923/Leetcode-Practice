class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum=nums[0] 
        maxsum=nums[0]  
        for num in nums[1:]:
            cur_sum=max(cur_sum+num, num)  
            maxsum=max(maxsum,cur_sum) 
        return maxsum