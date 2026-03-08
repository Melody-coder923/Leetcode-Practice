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
12        # Output: Construct a new linkedlist, val, next, random -> newlinedlist
13        # [val, random_index]
14        #Eduge CASE
15        if not head:
16            return None
17        #Step1 Build New node copy origial linkedlist
18        # map : old node -> new node  NewNode
19        map={}
20        cur=head
21        while cur:
22            map[cur]=Node(cur.val)
23            cur=cur.next
24        
25        #Step2: build new linkedlist relationship according to old one  Build
26        cur=head
27        while cur:
28            map[cur].next=map.get(cur.next)
29            map[cur].random=map.get(cur.random)
30            cur=cur.next
31        return map[head]
32
33
34
35
36
37
38
39        
40
41        