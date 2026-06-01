1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isValidBST(self, root: Optional[TreeNode]) -> bool:
9        if not root:
10                return True 
11
12        minValue=float("-inf")
13        maxValue=float("inf")
14        def dfs(node,minValue,maxValue):
15            if not node:
16                return True
17            if not (minValue < node.val < maxValue):
18                return False
19            left= dfs(node.left,minValue,node.val) 
20            right= dfs(node.right,node.val,maxValue)
21            return left and right
22            
23        return dfs(root,minValue,maxValue)
24