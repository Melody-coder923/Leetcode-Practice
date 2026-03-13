1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
9        
10        def dfs(p,q):
11            if not p and not q:
12                return True
13            if not p or not q or p.val!=q.val:
14                return False
15            return dfs(p.left,q.right) and dfs(p.right,q.left)
16        return dfs(root.left,root.right)