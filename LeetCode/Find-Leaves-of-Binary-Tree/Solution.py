1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
9        if not root:
10            return root
11        res=[]
12        #每个节点要知道自己高度
13        def dfs(node):
14            if not node:
15                return -1
16            left=dfs(node.left)
17            right=dfs(node.right)
18            height=max(left,right)+1
19            if height == len(res):
20                res.append([])
21            res[height].append(node.val)
22            return height
23
24        dfs(root)
25        return res