1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
9        if not root:
10            return None
11        cur=root
12        stack=[]
13        while cur or stack:
14            while cur:
15                stack.append(cur)
16                cur=cur.left
17            
18            node=stack.pop()
19            k-=1
20            if k==0:
21                return node.val
22            if node.right:
23                cur=node.right
24        