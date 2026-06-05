1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxDepth(self, root: Optional[TreeNode]) -> int:
9        max_depth=0
10        def dfs(node):
11            nonlocal max_depth
12            if not node:
13                return 0
14            left=dfs(node.left)
15            right=dfs(node.right)
16            max_depth=max(max_depth,left,right)
17            return max(left,right)+1
18        return dfs(root)