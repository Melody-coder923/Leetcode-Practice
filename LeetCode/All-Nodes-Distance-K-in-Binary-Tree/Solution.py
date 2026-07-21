1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution:
9    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
10        parent_map={}
11        def find_parent(node,parent):
12            if not node:
13                return
14            if node.left:
15                parent_map[node.left]=node
16                find_parent(node.left,node)
17            if node.right:
18                parent_map[node.right]=node
19                find_parent(node.right,node)
20        
21        find_parent(root,None)
22
23        q=deque([(target,0)])
24        visited={target}
25        res=[]
26        while q:
27            node,dis=q.popleft()
28            if dis==k:
29                res.append(node.val)
30                continue
31            for nei in [node.left,node.right,parent_map.get(node)]:
32                if nei and nei not in visited:
33                    q.append((nei,dis+1))
34                    visited.add(nei)
35        return res