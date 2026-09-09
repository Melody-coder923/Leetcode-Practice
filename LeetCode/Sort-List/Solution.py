1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        def merge(l1,l2):
9            dummy=ListNode(-1)
10            cur=dummy
11            while l1 and l2:
12                if l1.val<=l2.val:
13                    cur.next=l1
14                    l1=l1.next
15                else:
16                    cur.next=l2
17                    l2=l2.next
18                
19                cur=cur.next
20
21            if l1:
22                cur.next=l1
23            if l2:
24                cur.next=l2
25                
26            return dummy.next
27        
28
29        if not head or not head.next:
30            return head
31
32        fast=head.next
33        slow=head
34        while fast and fast.next:
35            fast=fast.next.next
36            slow=slow.next
37        
38        next_half=slow.next
39        slow.next=None
40        
41  
42        left=self.sortList(head)
43        right=self.sortList(next_half)
44
45        return merge(left,right)
46        
47