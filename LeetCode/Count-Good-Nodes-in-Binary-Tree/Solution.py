1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def goodNodes(self, root: TreeNode) -> int:
9        def dfs(node, maxval):
10            if not node:
11                return 0
12
13            if node.val >= maxval:
14                good = 1
15            else:
16                good = 0
17
18            maxval = max(maxval, node.val)
19
20            left = dfs(node.left, maxval)
21            right = dfs(node.right, maxval)
22
23            return good + left + right
24
25        return dfs(root, root.val)