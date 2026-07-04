1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isValidBST(self, root: Optional[TreeNode]) -> bool:
9        if not root:
10            return True
11        maxVal=float("inf")
12        minVal=float("-inf")
13        def dfs(node,maxVal,minVal):
14            if not node:
15                return True
16            if not (minVal < node.val < maxVal):
17                return False
18            return dfs(node.left,node.val,minVal) and dfs(node.right,maxVal,node.val)
19        return dfs(root,maxVal,minVal)