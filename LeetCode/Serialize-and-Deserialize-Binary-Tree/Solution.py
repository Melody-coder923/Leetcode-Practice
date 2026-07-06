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
18
19        res = []
20
21        def dfs(node):
22            if not node:
23                res.append("null")
24                return
25
26            res.append(str(node.val))
27            dfs(node.left)
28            dfs(node.right)
29
30        dfs(root)
31        return ",".join(res)
32
33    def deserialize(self, data):
34        """Decodes your encoded data to tree.
35        
36        :type data: str
37        :rtype: TreeNode
38        """
39        vals = data.split(",")
40        self.i = 0
41
42        def dfs():
43            if vals[self.i] == "null":
44                self.i += 1
45                return None
46
47            node = TreeNode(int(vals[self.i]))
48            self.i += 1
49
50            node.left = dfs()
51            node.right = dfs()
52
53            return node
54
55        return dfs()
56            
57
58# Your Codec object will be instantiated and called as such:
59# ser = Codec()
60# deser = Codec()
61# ans = deser.deserialize(ser.serialize(root))