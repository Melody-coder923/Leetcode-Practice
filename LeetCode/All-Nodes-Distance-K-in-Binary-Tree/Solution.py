1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7from collections import deque
8class Solution:
9    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
10        
11        #build parent relations
12        n_to_parent={}
13        def findparent(node):
14            if not node:
15                return
16            if node.left:
17                n_to_parent[node.left]=node
18                findparent(node.left)
19            if node.right:
20                n_to_parent[node.right]=node
21                findparent(node.right)
22        findparent(root)
23        #bfs
24        q=deque([(target,0)])
25        visited={target}
26        res=[]
27        while q:
28            for _ in range(len(q)):
29                node,dis=q.popleft()
30                if dis==k:
31                    res.append(node.val)
32                    continue
33                for nei in (node.left,node.right, n_to_parent.get(node)):
34                    if nei and nei not in visited:
35                        q.append((nei,dis+1))
36                        visited.add(nei)
37        return res