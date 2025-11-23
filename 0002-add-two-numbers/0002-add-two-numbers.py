# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # edge cases
        if not l1:
            return l2
        if not l2:
            return l1
        
        # 2 4 3 5,8
        # 5 6 4
        # while 遍历, or 
        dummy=ListNode(-1) # 新建
        p=dummy
        carry=0
        while l1 or l2 or carry:
            if l1: 
                a=l1.val
            else:
                a=0
            if l2:
                b=l2.val
            else:
                b=0
            total=a+b+carry # 2+5+0=7, 4+6+0=10, 3+4+1=8, 5
            carry= total//10 #0 , 1 , 0, 0
            mod= total%10  # 7 , 0 , 8, 5
            p.next= ListNode(mod) # dummy-> 7 -> 0-> 8 ->5
            p=p.next # dummy->7 -> 0-> 8 ->5
        
            if l1:  # 5,8
                l1=l1.next #5
            if l2:
                l2=l2.next
            if carry:
                p.next=ListNode(carry)

        return dummy.next