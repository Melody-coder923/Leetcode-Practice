1class Solution:
2    def trap(self, height: List[int]) -> int:
3        left,right=0,len(height)-1
4        maxLeft=maxRight=0
5        area=0
6        while left<right:
7            if height[left]<height[right]:
8                #如果遇到更高的，更新高度
9                if height[left]>maxLeft:
10                    maxLeft=height[left]
11                else:
12                    area+=maxLeft-height[left]
13                left+=1
14            else:
15                if height[right]>maxRight:
16                    maxRight=height[right]
17                else:
18                    area+=maxRight-height[right]
19                right-=1
20        return area