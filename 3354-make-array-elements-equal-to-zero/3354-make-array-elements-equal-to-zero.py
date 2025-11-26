class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        # Input: nums(given) ,curr (Random)
        """
        if nums[curr]==0:  direction:l or r  +2

        if  nums[curr]>0 : nums[curr]-1 , !!!direction: reverse, take a step  +1

        if curr over [0,n-1] : end +0
        """
        # Output: all become 0 and get number of valid selections
        
        leftsum=0
        total=sum(nums)
        count=0
        for num in nums:
            leftsum+=num
            if num==0:
                if leftsum==total-leftsum:
                    count+=2
                elif abs(leftsum-total+leftsum)==1:
                    count+=1
        return count
        