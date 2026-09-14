1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
9        if not root:
10            return 0
11        self.res=0
12
13        def dfs(node):
14            if not node:
15                return 0
16            
17            left=dfs(node.left)
18            right=dfs(node.right)
19
20            left_path=0
21            right_path=0
22
23            if node.left and node.left.val==node.val:
24                left_path=left+1
25            if node.right and node.right.val==node.val:
26                right_path=right+1
27
28
29            self.res=max(left_path+right_path,self.res)
30
31            return max(left_path,right_path)
32        
33        dfs(root)
34
35        return self.res