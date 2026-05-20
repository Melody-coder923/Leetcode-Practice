1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
9        res=None
10        def dfs(node):
11            nonlocal k,res
12            if not node or res is not None:
13                return
14            dfs(node.left)
15            k=k-1
16            if k==0:
17                res=node.val
18            dfs(node.right)
19        dfs(root)
20        return res