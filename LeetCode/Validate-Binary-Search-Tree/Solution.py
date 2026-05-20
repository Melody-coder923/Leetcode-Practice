1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isValidBST(self, root: Optional[TreeNode]) -> bool:
9        minValue=float('-inf')
10        maxValue=float('inf')
11        def helper(node,minValue,maxValue):
12            if not node:
13                return True
14            return minValue<node.val<maxValue and helper(node.left,minValue,node.val) and helper(node.right,node.val,maxValue)
15        return helper(root,minValue,maxValue)