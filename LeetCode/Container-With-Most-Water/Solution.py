1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        #who short who move
4        left,right=0,len(height)-1
5        maxarea=0
6        while left<right:
7            area=min(height[left],height[right])*(right-left)
8            maxarea=max(area,maxarea)
9            if height[left]<=height[right]:
10                left+=1
11            else:
12                right-=1
13        return maxarea
14