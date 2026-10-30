class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None

class LRUCache:
    def __init__(self, capacity: int):
        self.dict={}
        self.capacity=capacity
        self.size=0
        self.head=Node(-1,-1)
        self.tail=Node(-1,-1)
        self.head.next=self.tail
        self.tail.prev=self.head
    
    def detach(self,node):
        prev_node=node.prev
        nxt_node=node.next

        prev_node.next=nxt_node
        nxt_node.prev=prev_node


    def move_to_tail(self,node):
        prev_node=self.tail.prev
        prev_node.next=node
        node.prev=prev_node

        node.next=self.tail
        self.tail.prev=node

    def get(self, key: int) -> int:
        if key in self.dict:
            node=self.dict[key]
            self.detach(node)
            self.move_to_tail(node)
            return node.val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            node=self.dict[key]
            self.detach(node)
            self.move_to_tail(node)   
            node.val=value

        else: #新建
            new_node=Node(key,value)
        
            if self.size==self.capacity: # 尺寸满了
                remove_node=self.head.next
                self.detach(remove_node) 
                remove_key=remove_node.key
                del self.dict[remove_key]

                self.move_to_tail(new_node)
        
            
            else: #尺寸没满
                self.move_to_tail(new_node)
                self.size+=1

            self.dict[key] = new_node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)