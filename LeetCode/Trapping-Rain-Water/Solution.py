1class Solution:
2    def trap(self, height: List[int]) -> int:
3        l,r=0,len(height)-1
4        area=0
5        maxLeft=maxRight=0
6        while l<r:
7            if height[l]<height[r]:
8                if height[l]>maxLeft:
9                    maxLeft=height[l]
10                else:
11                    area+=maxLeft-height[l]
12                l+=1
13            else:
14                if height[r]>maxRight:
15                    maxRight = height[r]
16                else:
17                    area+=maxRight-height[r]
18                r-=1
19
20        return area