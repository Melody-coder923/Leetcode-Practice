1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
9        if not root:
10            return 
11        stack=[]
12        cur=root
13        while stack or cur:
14            while cur:
15                stack.append(cur)
16                cur=cur.left
17            node=stack.pop()
18            k-=1
19            if k==0:
20                return node.val
21            else:
22                if node and node.right:
23                    cur=node.right
24        return node.val
25
26            
27