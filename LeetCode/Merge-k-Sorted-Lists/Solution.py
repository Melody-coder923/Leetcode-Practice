1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6import heapq
7class Solution:
8    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
9        # Input: many sorted linkedlist
10        # Output: merge into one contraint: sorted
11        # min_heap-> newlinkedlist
12
13        if len(lists)==0:
14            return None
15        if len(lists)==1:
16            return lists[0]
17
18        heap=[]
19        dummy=ListNode(0)
20        cur=dummy
21
22        for i,node in enumerate(lists):
23            if node:
24                heapq.heappush(heap,(node.val,i,node))
25        
26        while heap:
27            val,i,node=heapq.heappop(heap)
28            cur.next=node
29            cur=cur.next
30
31            if node.next: 
32                next_node=node.next
33                heapq.heappush(heap,(next_node.val,i,next_node))
34
35        return dummy.next