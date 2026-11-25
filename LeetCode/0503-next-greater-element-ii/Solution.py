class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        stack=[]
        res=[-1]*n

        for i in range(n*2):
            cur=nums[i%n]
            while stack and nums[stack[-1]]<cur:
                res[stack.pop()] = cur
            if i<n:
                stack.append(i)

        return res