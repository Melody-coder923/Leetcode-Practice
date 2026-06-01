1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution:
9    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
10        if not root:
11            return None
12        if root==p or root==q:
13            return root
14        left=self.lowestCommonAncestor(root.left,p,q)
15        right=self.lowestCommonAncestor(root.right,p,q)
16        if left and right:
17            return root
18        if left:
19            return left
20        if right:
21            return right
22        return None