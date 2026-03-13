1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
9        def helper(p,q):
10            if not p and not q:
11                return True
12            if not p or not q or p.val!=q.val:
13                return False
14            return helper(p.left,q.right) and helper(p.right,q.left)
15        if not root:
16            return True
17        return helper(root.left,root.right)
18
19    
20    