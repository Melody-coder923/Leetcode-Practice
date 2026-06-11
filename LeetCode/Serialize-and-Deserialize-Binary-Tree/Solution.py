1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Codec:
9
10    def serialize(self, root):
11        """Encodes a tree to a single string.
12        
13        :type root: TreeNode
14        :rtype: str
15        """
16        if not root:
17            return "null"
18        res=[]
19        def dfs(node):
20            if not node:
21                res.append("null")
22                return
23            res.append(str(node.val))
24            dfs(node.left)
25            dfs(node.right)
26        dfs(root)
27        return ",".join(res)
28            
29    def deserialize(self, data):
30        """Decodes your encoded data to tree.
31        
32        :type data: str
33        :rtype: TreeNode
34        """
35        if not data:
36            return None
37        vals = data.split(",")
38        i=0
39        def dfs():
40            nonlocal i
41            if i==len(vals):
42                return 
43            if vals[i] == "null":
44                i += 1
45                return None           
46            root = TreeNode(int(vals[i]))
47            i += 1
48            root.left=dfs()
49            root.right=dfs()
50            
51            return root
52        return dfs()
53            
54
55# Your Codec object will be instantiated and called as such:
56# ser = Codec()
57# deser = Codec()
58# ans = deser.deserialize(ser.serialize(root))