1class Solution:
2    def largestRectangleArea(self, heights: List[int]) -> int:
3        heights.append(0)
4        n = len(heights)
5        stack=[]
6        maxarea=0
7        for i,num in enumerate(heights):
8            while stack and heights[stack[-1]]>num:
9                top_idx=stack.pop()
10                h=heights[top_idx]
11                # i-1-(stack[-1]+1)+1=i-stack[-1]-1
12                width=i if not stack else i-stack[-1]-1
13                area=h*width
14                maxarea=max(area,maxarea)
15            stack.append(i)
16        return maxarea