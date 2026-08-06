1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
9        def sametree(p,q):
10            if not p and not q:
11                return True
12            if not p or not q or p.val!=q.val:
13                return False
14            
15            return sametree(p.left,q.left) and sametree(p.right,q.right)
16
17        if not root:
18            return False
19    
20        return sametree(root,subRoot) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)