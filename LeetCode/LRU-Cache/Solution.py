1class Node:
2    def __init__(self,key,value):
3        self.key=key
4        self.val=value
5        self.prev=None
6        self.next=None
7
8class LRUCache:
9    def __init__(self, capacity: int):
10        self.capacity=capacity
11        self.size=0
12        self.head=Node(0,0)
13        self.tail=Node(0,0)
14        self.head.next=self.tail
15        self.tail.prev=self.head
16        self.map={} # key-> node
17    
18    # (不常用)head-1-3-4-5-2-tail(常用)
19    def detach(self,node): #前后断开
20        prev_node=node.prev
21        next_node=node.next
22        prev_node.next=next_node
23        next_node.prev=prev_node
24
25    def move_to_tail(self,node): 
26        node.next=self.tail
27        node.prev=self.tail.prev
28        self.tail.prev.next=node
29        self.tail.prev=node
30    
31    def add(self,node,is_new=False):
32        self.move_to_tail(node)
33        if is_new:
34            self.size+=1
35
36    def delete(self,node): #空间满需要删除
37        self.detach(node)
38        self.size-=1
39        
40    def get(self, key: int) -> int:
41        if key in self.map:
42            node=self.map[key]
43            self.detach(node)
44            self.move_to_tail(node)
45            return node.val
46        return -1
47    def put(self, key: int, value: int) -> None:
48        if key in self.map:
49            node=self.map[key]
50            node.val=value
51            self.detach(node)
52            self.move_to_tail(node)
53        else:
54            new_node=Node(key,value)
55            if self.capacity==self.size:
56                temp=self.head.next
57                del self.map[temp.key]
58                self.delete(temp)
59            self.map[key] = new_node  
60            self.add(new_node, is_new=True)
61
62                            
63# Your LRUCache object will be instantiated and called as such:
64# obj = LRUCache(capacity)
65# param_1 = obj.get(key)
66# obj.put(key,value)