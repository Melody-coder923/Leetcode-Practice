1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8from collections import deque
9class Solution:
10    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
11        if not root:
12            return []
13        res=[]
14        que=deque([root])
15        while que:
16            size=len(que)
17            for i in range(size):
18                node=que.popleft()
19                if node.left:
20                    que.append(node.left)
21                if node.right:
22                    que.append(node.right)
23                if i==size-1:
24                    res.append(node.val)
25        return res
26        