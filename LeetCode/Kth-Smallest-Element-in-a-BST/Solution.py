1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:   
9        self.k = k
10        self.ans = None
11
12        def dfs(root):
13            if not root:
14                return
15            dfs(root.left)
16            self.k -= 1
17            if self.k == 0:
18                self.ans = root.val
19                return
20            dfs(root.right)
21
22        dfs(root)
23        return self.ans