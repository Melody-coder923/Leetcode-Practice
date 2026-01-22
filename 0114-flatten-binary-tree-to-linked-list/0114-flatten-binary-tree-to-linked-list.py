# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        right=root.right
        left=root.left

        root.left=None
        root.right=left

        #1->left- right
        cur=root
        while cur.right: # cur停在有节点位置
            cur=cur.right #挪动指针 
        # left finish
        cur.right=right # 接right整体
    