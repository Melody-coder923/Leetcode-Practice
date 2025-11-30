# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None  # 安全检查
        # 反转 1->2   2->1
        def reverse(head):
            prev=None
            curr=head
            while curr:
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            return prev

        # 找到分组,快慢指针
        fast=slow=head
        for _ in range(k-1):
            if not fast.next:  # 剩余节点不足 k 个
                return head
            fast = fast.next

        nextround=fast.next
        fast.next=None
        newhead= reverse(slow)
    
        
        # 链接分组反转 + 递归
        slow.next=self.reverseKGroup(nextround,k)
        return newhead