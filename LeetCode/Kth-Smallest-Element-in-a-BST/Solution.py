1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
9        stack=[]
10        curr=root
11        while curr or stack:
12            while curr:
13                stack.append(curr)
14                curr=curr.left
15            curr=stack.pop()
16            k-=1
17            if k==0:
18                return curr.val
19            curr=curr.right