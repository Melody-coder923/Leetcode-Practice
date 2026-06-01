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
16        def dfs(node):
17            if not node:
18                return "null,"
19            return str(node.val) + "," + dfs(node.left) + dfs(node.right)
20        
21        return dfs(root)
22
23    def deserialize(self, data):
24        """Decodes your encoded data to tree.
25        
26        :type data: str
27        :rtype: TreeNode
28        """
29        # 把字符串转成列表
30        vals = data.split(",")
31        self.index = 0
32
33        def dfs():
34            if vals[self.index] == "null":
35                self.index += 1
36                return None
37            node = TreeNode(int(vals[self.index]))
38            self.index += 1
39            node.left = dfs()
40            node.right = dfs()
41            return node
42
43        return dfs()
44        
45
46# Your Codec object will be instantiated and called as such:
47# ser = Codec()
48# deser = Codec()
49# ans = deser.deserialize(ser.serialize(root))