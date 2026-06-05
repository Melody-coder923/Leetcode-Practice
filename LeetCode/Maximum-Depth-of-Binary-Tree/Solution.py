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
11        queue=collections.deque([root])
12        count=0
13        while queue:
14            level_size=len(queue)
15            for _ in range(level_size):
16                node=queue.popleft()
17                if node.left:
18                    queue.append(node.left)
19                if node.right:
20                    queue.append(node.right)
21            count+=1
22        return count
23        
24        