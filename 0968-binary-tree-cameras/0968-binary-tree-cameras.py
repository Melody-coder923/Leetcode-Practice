# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#状态 0：需要被覆盖（没人管我) 状态 1：已被覆盖（被子节点的摄像头照到）│状态 2：有摄像头（我自己有摄像头）   
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.cameras = 0
        def helper(node):
            if not node:
                return 1
            left=helper(node.left)
            right=helper(node.right)

            # 子节点需要覆盖 → 放摄像头
            if left==0 or right==0:
                self.cameras+=1
                return 2
            # 子节点有摄像头 → 被覆盖
            if left==2 or right==2:
                return 1
            # 否则 → 需要被覆盖
            return 0
        # 根节点特殊处理
        if helper(root)==0:
            self.cameras+=1

        return self.cameras