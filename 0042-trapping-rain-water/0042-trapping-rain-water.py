class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        area = 0
        #栈中对应的高度是「单调递减」的
        #栈里放的是“还没等到右墙的柱子”， 一旦遇到更高的柱子，就不断结算它们上面的水。
        for cur in range(len(height)):
            #开始接水
            while stack and height[cur] > height[stack[-1]]:
                bottom = stack.pop()
                if not stack:
                    break
                
                left = stack[-1]
                width = cur - left - 1
                bounded_height = min(height[left], height[cur]) - height[bottom]

                area += width * bounded_height

            stack.append(cur)

        return area

