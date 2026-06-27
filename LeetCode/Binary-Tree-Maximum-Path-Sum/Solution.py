1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxPathSum(self, root: Optional[TreeNode]) -> int:
9        if not root:
10            return 0
11        maxpath=float("-inf")
12        def dfs(node):
13            nonlocal maxpath
14            if not node:
15                return 0
16            left=max(0,dfs(node.left))
17            right=max(0,dfs(node.right))
18            maxpath=max(maxpath,left+right+node.val)
19            return max(left,right)+node.val
20        
21        dfs(root)
22        return maxpath
23
24