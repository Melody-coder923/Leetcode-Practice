1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6import heapq
7class Solution:
8    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
9        if not lists:
10            return None
11        heap=[]
12        dummy=ListNode(0)
13        cur=dummy
14
15        for i,node in enumerate(lists):
16            if node:
17                heapq.heappush(heap,(node.val,i,node))
18        
19        while heap:
20            val,i,node=heapq.heappop(heap)
21            cur.next=node
22            cur=cur.next
23
24            if node.next:
25                heapq.heappush(heap,(node.next.val,i,node.next))
26        
27        return dummy.next