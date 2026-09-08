1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
9        if not root or not root.left:
10                return root
11
12        new_root = self.upsideDownBinaryTree(root.left)
13
14        left_child = root.left
15        left_child.left = root.right
16        left_child.right = root
17
18        root.left = None
19        root.right = None
20
21        return new_root
22