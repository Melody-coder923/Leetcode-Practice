1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isBalanced(self, root: Optional[TreeNode]) -> bool:
9        balanced=True
10        def help(node):
11            nonlocal balanced
12            if not node:
13                return 0
14            left=help(node.left)
15            right=help(node.right)
16            if abs(left-right)>1:
17                balanced=False
18            return max(left,right)+1
19        help(root)
20        return balanced