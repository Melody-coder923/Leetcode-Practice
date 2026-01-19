# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Input: many sorted linkedlist
        # Output: merge into one contraint: sorted
        # min_heap-> newlinkedlist

        if len(lists)==0:
            return None
        if len(lists)==1:
            return lists[0]

        heap=[]
        dummy=ListNode(0)
        cur=dummy

        for i,node in enumerate(lists):
            if node:
                heapq.heappush(heap,(node.val,i,node))
        
        while heap:
            val,i,node=heapq.heappop(heap)
            cur.next=node
            cur=cur.next

            if node.next: 
                next_node=node.next
                heapq.heappush(heap,(next_node.val,i,next_node))

        return dummy.next