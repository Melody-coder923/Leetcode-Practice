1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6import heapq
7class Solution:
8    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
9        heap=[]
10        dummy=ListNode(-1)
11        cur=dummy
12
13        for i,node in enumerate(lists):
14            if node:
15                heapq.heappush(heap,(node.val,i,node))
16
17        while heap:
18            val,i,node=heapq.heappop(heap)
19            cur.next=node
20            cur=cur.next
21            if node.next:
22                heapq.heappush(heap, (node.next.val,i,node.next))
23        
24        return dummy.next
25            