1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
8        heap=[]
9        for i,node in enumerate(lists):
10            if node:
11                heapq.heappush(heap,(node.val,i,node))
12        dummy=ListNode(-1)
13        curr=dummy
14        while heap:
15            value,i,node=heapq.heappop(heap)
16            curr.next=node
17            curr=curr.next
18            if node.next:
19                nxt=node.next
20                heapq.heappush(heap,(nxt.val,i,nxt))
21        
22        return dummy.next