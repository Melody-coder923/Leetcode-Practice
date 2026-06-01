1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
9        def isSame(p,q):
10            if not p and not q:
11                return True
12            if not p or not q or p.val!=q.val:
13                return False
14            return p.val==q.val and isSame(p.left,q.left) and isSame(p.right,q.right)
15        if not root:
16            return False
17        
18        return isSame(root,subRoot) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)