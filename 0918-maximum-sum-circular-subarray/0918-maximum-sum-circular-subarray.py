class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = 0
        cur_max = 0
        best = float('-inf')
        cur_min = 0
        mintotal = float('inf')

        for num in nums:
        # option 1: max subarry in nums - traditioanl way to get max subarr
            cur_max = max(num, cur_max + num)
            best = max(best, cur_max)
        # option 2:  max subarry in circle joint area - tradional way to get min subarr
            cur_min = min(num, cur_min + num)
            mintotal = min(mintotal, cur_min)
    
            total+=num
        
        if best > 0:
            return max(best, total - mintotal)
        else:
            return best
        