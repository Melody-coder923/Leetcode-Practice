"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # 第一步：建立旧节点 → 新节点映射
        node_map = {}
        cur = head
        while cur:
            node_map[cur] = Node(cur.val)
            cur = cur.next

        # 第二步：构建 next 和 random 指向
        cur = head
        while cur:
            node_map[cur].next = node_map.get(cur.next)       # 如果 cur.next 是 None，get 返回 None
            node_map[cur].random = node_map.get(cur.random)   # 如果 cur.random 是 None，get 返回 None
            cur = cur.next

        # 返回新链表头
        return node_map[head]