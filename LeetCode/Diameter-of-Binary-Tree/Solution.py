1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
9        if not root:
10            return 0
11        res=0
12        def dfs(node):
13            nonlocal res
14            if not node:
15                return 0
16            left=dfs(node.left)
17            right=dfs(node.right)
18            res=max(res,left+right)
19            return max(left,right)+1
20        dfs(root)
21        return res