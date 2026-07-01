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
24        # bfs
25        q=deque([(target,0)])
26        visited={target}
27        res=[]
28        while q:
29            size=len(q)
30            for _ in range(size):
31                node,dis=q.popleft()
32                if dis==k:
33                    res.append(node.val)
34                    continue
35                for nxt in (node.left,node.right,n_to_parent.get(node)):
36                    if nxt and nxt not in visited:
37                        q.append((nxt,dis+1))
38                        visited.add(nxt)
39        return res