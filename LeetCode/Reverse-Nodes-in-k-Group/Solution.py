1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
8    
9        def reverse(node): 
10            prev=None 
11            while node:  
12                nxt=node.next   
13                node.next=prev
14                prev=node
15                node=nxt
16            
17            return prev
18        
19        if not head:
20            return 
21
22        fast=slow=head 
23        for _ in range(k-1):
24            if not fast.next:
25                return slow
26            fast=fast.next
27        
28        next_group_head=fast.next
29        fast.next=None
30        
31        new_first_half=reverse(slow)
32        #connect next_half_head
33        slow.next=next_group_head
34
35        
36        #怎么接
37        head.next=self.reverseKGroup(next_group_head,k)
38
39        return new_first_half
40
41