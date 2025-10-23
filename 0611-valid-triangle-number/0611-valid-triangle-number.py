class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # Step1:sort ,  Step2: a+b>c 
        nums.sort()
        n=len(nums)
        count=0
        for k in range(n-1,-1,-1):
            i,j=0,k-1
            while i<j:
                if nums[i]+nums[j]>nums[k]:
                    #all i to j-1 could form triangle
                    count+=j-i
                    j-=1
                else:
                    i+=1
        return count