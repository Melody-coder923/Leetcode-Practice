1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
9        if not root:
10            return 
11        lst=[]
12        def dfs(node):
13            if not node:
14                return
15            dfs(node.left)
16            lst.append(node.val)
17            dfs(node.right)
18            return lst
19        dfs(root)
20        return lst[k-1]
21            