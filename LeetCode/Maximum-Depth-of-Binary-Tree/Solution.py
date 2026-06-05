1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxDepth(self, root: Optional[TreeNode]) -> int:
9        if not root:
10            return 0
11        q=deque([root])
12        level=0
13        while q:
14            level+=1
15            size=len(q)
16            for _ in range(size):
17                node=q.popleft()
18                if node.left:
19                    q.append(node.left)
20                if node.right:
21                    q.append(node.right)
22        return level
23