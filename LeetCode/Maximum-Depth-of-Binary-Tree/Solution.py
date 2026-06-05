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
14            for _ in range(len(q)):
15                node=q.popleft()
16                if node.left:
17                    q.append(node.left)
18                if node.right:
19                    q.append(node.right)
20            level+=1
21        return level
22            