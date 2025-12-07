class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farest=0
        for i in range(len(nums)):
            farest = max(farest, nums[i] + i)
            if i>farest:
                return False
            
            if farest>=len(nums)-1:
                return True
        
        return True