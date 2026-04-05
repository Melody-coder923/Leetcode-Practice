1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
9        if not inorder or not postorder:
10            return 
11        root_val=postorder.pop()
12        root=TreeNode(root_val)
13        idx=inorder.index(root_val)
14        root.right= self.buildTree(inorder[idx+1:],postorder)
15        root.left= self.buildTree(inorder[:idx],postorder)
16        return root
17
18    
19    