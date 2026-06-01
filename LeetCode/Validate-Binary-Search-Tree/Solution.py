1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isValidBST(self, root: Optional[TreeNode]) -> bool:
9        stack = []
10        prev = float('-inf')
11        cur=root
12        while stack or cur:
13            while cur:
14                stack.append(cur)
15                cur = cur.left
16            node = stack.pop()
17            if node.val <= prev:
18                return False
19            prev =node.val
20            cur = node.right
21        return True