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
11        maxval=float("inf")
12        minval=float("-inf")
13        def dfs(node,maxval,minval):
14            if not node:
15                return True
16            if not(minval<node.val<maxval):
17                return False
18            left=dfs(node.left,node.val,minval)
19            right=dfs(node.right,maxval,node.val)
20            if left and right:
21                return True
22            return False
23        return dfs(root,maxval,minval)