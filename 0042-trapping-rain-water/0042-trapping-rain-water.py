class Solution:
    def trap(self, height: List[int]) -> int:
        left,right=0,len(height)-1
        maxleft=maxright=0
        area=0
        
        while left<right:
            if height[left]<=height[right]:
                maxleft=max(maxleft,height[left])
                area+= maxleft-height[left]
                left+=1

            elif height[left]>height[right]:
                maxright=max(maxright,height[right])
                area+= maxright-height[right]
                right-=1

        return area
