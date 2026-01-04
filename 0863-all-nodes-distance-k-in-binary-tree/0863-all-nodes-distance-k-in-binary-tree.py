# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # 建立父亲关系
        map={} #key node -> parent node
        def buildparent(node,parent):
            if not node:
                return 
            map[node]=parent
            buildparent(node.left,node)
            buildparent(node.right,node)
        
        buildparent(root,None)
        
        #BFS  node,distance
        q=deque([(target,0)])
        visited={target}
        res=[]
        while q:
            node,distance=q.popleft()
            if distance==k:
                res.append(node.val)
            elif distance>k:
                continue
            for neighbor in [node.left,node.right,map.get(node)]:
                if neighbor and neighbor not in visited:
                    q.append((neighbor,distance+1))
                    visited.add(neighbor)
            
        return res