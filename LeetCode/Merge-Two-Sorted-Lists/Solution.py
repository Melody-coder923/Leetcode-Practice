1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:   
8        p1=list1
9        p2=list2
10        dummy=ListNode(-1)
11        curr=dummy
12        while p1 and p2:
13            if p1.val<=p2.val:
14                curr.next=p1
15                p1=p1.next
16            else:
17                curr.next=p2
18                p2=p2.next
19            curr=curr.next
20        
21        if p1:
22            curr.next=p1
23        if p2:
24            curr.next=p2
25        
26        return dummy.next
27                
28