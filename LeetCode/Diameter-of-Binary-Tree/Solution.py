1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
9        res=0
10        def dfs(node):
11            nonlocal res
12            if not node:
13                return 0
14            left=dfs(node.left)
15            right=dfs(node.right)
16            res=max(res,left+right)
17            return max(left,right) +1
18
19        dfs(root)
20        return res