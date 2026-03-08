1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
8        if not head or not head.next:
9            return head
10        dummy=ListNode(-1)
11        dummy.next=head
12        prev=dummy
13        #找left的前一个节点
14        for _ in range(left-1): 
15            prev=prev.next
16        
17        cur=prev.next # 这是开始需要交换的点
18        for _ in range(right - left):
19        #   prev   cur        nxt    nxt.next
20        #   prev  nxt.next    nxt    cur
21            nxt = cur.next 
22            cur.next = nxt.next
23            #往前接上
24            nxt.next = prev.next 
25            prev.next = nxt
26        
27        return dummy.next
28            