1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
9        if not root:
10            return True 
11        def mirror(p,q):
12            if not p and not q:
13                return True
14            if not p or not q or p.val!=q.val:
15                return False
16            return mirror(p.left,q.right) and mirror(p.right,q.left)
17        return mirror(root.left,root.right)
18            
19            