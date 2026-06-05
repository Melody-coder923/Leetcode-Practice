1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxDepth(self, root: Optional[TreeNode]) -> int:
9        if not root:
10            return 0
11        maxdepth=0
12        def dfs(node,depth):
13            nonlocal maxdepth
14            if not node:
15                return 0
16            maxdepth=max(maxdepth,depth)
17            dfs(node.left,depth+1)
18            dfs(node.right,depth+1)
19        dfs(root,1)
20        return maxdepth
21            
22