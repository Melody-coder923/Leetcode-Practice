1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
9
10        def dfs(node):
11            nonlocal k
12            if not node:
13                return
14            left=dfs(node.left)
15            if left is not None:
16                return left
17            k=k-1
18            if k==0:
19                return node.val
20            return dfs(node.right)
21        return dfs(root)