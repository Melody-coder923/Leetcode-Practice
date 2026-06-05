1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
9        if not root:
10            return False
11
12        def issame(p,q):
13            if not p and not q:
14                return True
15            if not p or not q or p.val!=q.val:
16                return False
17            return issame(p.left,q.left) and issame(p.right,q.right)
18        
19        return issame(root,subRoot) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
20
21        