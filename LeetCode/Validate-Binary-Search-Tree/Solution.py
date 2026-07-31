1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isValidBST(self, root: Optional[TreeNode]) -> bool:
9        minVal=float("-inf")
10        maxVal=float("inf")
11        def dfs(node,minVal,maxVal):
12            if not node:
13                return True
14            if not minVal<node.val<maxVal:
15                return False
16        
17            return dfs(node.left,minVal,node.val) and dfs(node.right,node.val,maxVal)
18
19        return dfs(root,minVal,maxVal)
20
21        