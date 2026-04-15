1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    # 求count
9    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int: #return targetSum
10        prefix=defaultdict(int)
11        prefix[0] = 1
12        count=0
13        def dfs(node,curSum):
14            nonlocal count
15            if not node:
16                return 
17            curSum+=node.val
18            if curSum - targetSum in prefix:
19                count += prefix[curSum - targetSum]
20            prefix[curSum]+=1
21            dfs(node.left,curSum)
22            dfs(node.right,curSum)
23            prefix[curSum] -= 1
24        dfs(root, 0)
25        return count
26            
27            
28
29
30
31            