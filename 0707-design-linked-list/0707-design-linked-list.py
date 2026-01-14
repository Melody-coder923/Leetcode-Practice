class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.size=0
        self.head=ListNode(0)

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        cur = self.head.next
        for _ in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)      
        new_node.next = self.head.next 
        self.head.next = new_node       
        self.size += 1                  


    def addAtTail(self, val: int) -> None:
        cur=self.head
        while cur.next:
            cur=cur.next
        prev_last=cur
        new_node=ListNode(val)
        prev_last.next=new_node
        self.size +=1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index < 0:
            index = 0
        prev = self.head
        for _ in range(index):
            prev = prev.next
        new_node = ListNode(val)
        new_node.next = prev.next
        prev.next = new_node
        self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        prev = self.head
        for _ in range(index):
            prev = prev.next
        prev.next = prev.next.next
        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)