1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
9        if not root:
10            return root
11        
12        def dfs(node):
13            if not node:
14                return
15            node.left,node.right=node.right,node.left
16            dfs(node.left)
17            dfs(node.right)
18
19        dfs(root)
20        
21        return root