class Node:
    def __init__(self, key: int, value: int):
        self.key=key
        self.val=value
        self.prev=None
        self.next=None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.size=0
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.map={}
        
    # 从链表中断开节点（仅断链，不删 map，不改 size）
    def detach(self,node):
        prev_node=node.prev
        next_node=node.next
        prev_node.next=next_node
        next_node.prev=prev_node

    # 将节点插入到尾部（最近使用）
    def add(self,node, is_new:bool=True):
        node.next=self.tail
        node.prev=self.tail.prev

        self.tail.prev.next=node
        self.tail.prev=node
        if is_new:
            self.size+=1
      
    # 删除节点（用于超容量删除）
    def del_node(self,node):
        self.detach(node)
        del self.map[node.key]
        self.size-=1
        
   
    # 移动节点到尾部（最近使用，不改变 size）
    def move_to_tail(self,node):
        self.detach(node)
        self.add(node,is_new=False)

   
    # get 操作
    def get(self,key):
        if key not in self.map:
            return -1
        self.move_to_tail(self.map[key])
        return self.map[key].val
        
    # put 操作
    def put(self,key,value):
        if key in self.map:
            self.move_to_tail(self.map[key])
            self.map[key].val=value
        else:
            if self.size==self.capacity:
                self.del_node(self.head.next)
            new_node=Node(key,value)
            self.add(new_node,is_new=True)
            self.map[key]=new_node
            

       