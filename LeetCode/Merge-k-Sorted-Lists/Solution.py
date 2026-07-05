1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
8        heap=[]
9        for idx, node in enumerate(lists):
10            if node:
11                heapq.heappush(heap, (node.val, idx, node))
12        
13        newlist=ListNode(0)
14        cur=newlist
15        while heap:
16            val,idx,node=heapq.heappop(heap)
17            cur.next = node
18            cur = cur.next
19            if node.next:
20                nxt=node.next
21                heapq.heappush(heap,(nxt.val,idx,nxt))
22        
23        return newlist.next