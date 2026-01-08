class Solution:
    def trap(self, height: List[int]) -> int:
        stack=[0]
        area=0
        #高-低-高可以接水 - 单调递减栈, 直到遇到高的开始接水
        for i in range(1,len(height)):
           #找到比栈顶更高的了,开始节水
            while stack and height[stack[-1]]<height[i]:
                bottom=stack.pop()
                if not stack:
                    break
                left=stack[-1]
                width = i - left - 1 #left 和 i 两端柱子本身不能算水槽宽度,只有中间位置才能算,所以是-1
                #限制高-当前的高度
                bounded_height = min(height[left], height[i]) - height[bottom]
                area += width * bounded_height
            #递减就继续加如栈
            stack.append(i)
        return area
                

                
