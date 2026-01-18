"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def build(x,y,size):
            if self.allsame(grid,x,y,size):
                return Node(val=grid[x][y]==1,isLeaf=True)
            half=size//2
            topLeft = build(x, y, half)                    # 左上
            topRight = build(x, y + half, half)            # 右上
            bottomLeft = build(x + half, y, half)          # 左下
            bottomRight = build(x + half, y + half, half)  # 右下
            # 合并：创建非叶子节点
            return Node(val=1, isLeaf=False, 
                       topLeft=topLeft, topRight=topRight,
                       bottomLeft=bottomLeft, bottomRight=bottomRight)

        return build(0, 0, len(grid))
    def allsame(self,grid,x,y,size):
        first_val = grid[x][y]
        for i in range(x,x+size):
            for j in range(y,y+size):
                if grid[i][j]!=first_val:
                    return False
        return True







