1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution:
9    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
10        #build parent relations
11        n_to_parent = {}
12
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
23
24        q=deque([(target,0)])
25        res=[]
26        visited={target}
27        while q:
28            size=len(q)
29            for _ in range(size):
30                node,dis=q.popleft()
31                if dis==k:
32                    res.append(node.val)
33                    continue
34                for nxt in (node.left, node.right,n_to_parent.get(node)):
35                    if nxt and nxt not in visited:
36                        q.append((nxt,dis+1))
37                        visited.add(nxt)
38        return res