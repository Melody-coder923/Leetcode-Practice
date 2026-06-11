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
16            left=dfs(node.left,node.val,minval)
17            right=dfs(node.right,maxval,node.val)
18            if left and right and minval<node.val<maxval:
19                return True
20            return False
21        return dfs(root,maxval,minval)