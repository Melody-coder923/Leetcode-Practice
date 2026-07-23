1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
9        cur=root
10        stack=[]
11        while cur or stack:
12            while cur:
13                stack.append(cur)
14                cur=cur.left
15            cur=stack.pop()
16            k-=1
17            if k==0:
18                return cur.val 
19            cur=cur.right