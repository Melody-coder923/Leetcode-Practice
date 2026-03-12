1class Node:
2    def __init__(self,key,value):
3        self.key=key
4        self.val=value
5        self.prev=None
6        self.next=None
7
8class LRUCache:
9
10    def __init__(self, capacity: int):
11        self.capacity=capacity
12        self.map={}
13        self.head=Node(0,0)
14        self.tail=Node(0,0)
15        self.head.next=self.tail
16        self.tail.prev=self.head
17        self.size=0
18    
19    def detach(self,node):
20        prev_node=node.prev
21        next_node=node.next
22
23        prev_node.next=next_node
24        next_node.prev=prev_node
25        # 没从map删除
26    def add(self,node):
27        node.next=self.tail
28        prev_node=self.tail.prev
29        node.prev=prev_node
30
31        prev_node.next=node
32        self.tail.prev=node
33        #没增加map
34
35    def get(self, key: int) -> int:
36        if key not in self.map:
37            return -1
38        #如果在里面
39        node=self.map[key]
40        #move node到最后，先删，再补
41        self.detach(node)
42        self.add(node)
43        return node.val
44
45    def put(self, key: int, value: int) -> None:
46        if key in self.map:
47            node=self.map[key]
48            node.val=value
49            self.detach(node)
50            self.add(node)
51        else:
52            new_node = Node(key, value)
53            if self.size== self.capacity:
54                del self.map[self.head.next.key]
55                self.detach(self.head.next)
56                self.add(new_node)
57            else:
58                self.add(new_node)
59                self.size+=1
60
61            self.map[key]=new_node
62            
63            
64            
65
66
67# Your LRUCache object will be instantiated and called as such:
68# obj = LRUCache(capacity)
69# param_1 = obj.get(key)
70# obj.put(key,value)