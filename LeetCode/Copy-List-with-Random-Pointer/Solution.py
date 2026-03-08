1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
5        self.val = int(x)
6        self.next = next
7        self.random = random
8"""
9
10class Solution:
11    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
12        if not head:
13            return None
14
15        # 第一步：建立旧节点 → 新节点映射
16        node_map = {}
17        cur = head
18        while cur:
19            node_map[cur] = Node(cur.val)
20            cur = cur.next
21
22        # 第二步：构建 next 和 random 指向
23        cur = head
24        while cur:
25            node_map[cur].next = node_map.get(cur.next)       # 如果 cur.next 是 None，get 返回 None
26            node_map[cur].random = node_map.get(cur.random)   # 如果 cur.random 是 None，get 返回 None
27            cur = cur.next
28
29        # 返回新链表头
30        return node_map[head]