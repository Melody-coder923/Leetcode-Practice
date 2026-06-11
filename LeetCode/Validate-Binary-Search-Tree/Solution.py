1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isValidBST(self, root: Optional[TreeNode]) -> bool:
9        minValue=float("-inf")
10        maxValue=float("inf")
11        def dfs(node,minValue,maxValue):
12            if not node:
13                return True
14            if not (minValue < node.val < maxValue):
15                return False
16            left= dfs(node.left,minValue,node.val) 
17            right= dfs(node.right,node.val,maxValue)
18            return left and right
19        return dfs(root,minValue,maxValue)