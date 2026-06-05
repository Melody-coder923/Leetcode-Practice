1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isBalanced(self, root: Optional[TreeNode]) -> bool:
9        if not root:
10            return True
11        def help(node):
12            if not node:
13                return 0
14            left=help(node.left)
15            if left==-1:
16                return -1
17            right=help(node.right)
18            if right==-1:
19                return -1
20            if abs(left-right)>1:
21                return -1
22            return max(left,right)+1
23        return help(root) != -1