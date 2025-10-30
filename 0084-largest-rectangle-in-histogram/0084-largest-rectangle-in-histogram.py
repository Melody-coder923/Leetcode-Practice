class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0) #哨兵
        stack=[]
        maxarea=0
        for i,h in enumerate(heights):
            while stack and h<heights[stack[-1]]:
                top_index = stack.pop()
                height = heights[top_index]
                width = i if not stack else i - stack[-1] - 1
                maxarea=max(maxarea,height*width)
            stack.append(i)

        return maxarea