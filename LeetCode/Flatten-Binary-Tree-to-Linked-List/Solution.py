1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def flatten(self, root: Optional[TreeNode]) -> None:
9        """
10        Do not return anything, modify root in-place instead.
11        """
12        cur=root
13        while cur:
14            if cur.left:
15                rightmost=cur.left
16                while rightmost.right:
17                    rightmost=rightmost.right
18                rightmost.right=cur.right
19                cur.right=cur.left
20                cur.left=None
21            
22            cur=cur.right