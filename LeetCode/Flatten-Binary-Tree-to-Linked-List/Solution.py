1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def flatten(self, root: Optional[TreeNode]) -> None:
9        """
10        Do not return anything, modify root in-place instead.
11        """
12        def dfs(node):
13            if not node:
14                return
15            dfs(node.left)
16            dfs(node.right)
17            if node.left:
18                cur=node.left
19                while cur.right:
20                    cur=cur.right
21                cur.right=node.right
22                node.right=node.left
23                node.left=None
24        dfs(root)
25