1# O(1): dict key-val(node)
2# linkedlist->doublelinkedlist 
3class Node:
4    def __init__(self,key,val):
5        self.key=key
6        self.val=val
7        self.prev=None
8        self.next=None
9
10class LRUCache:
11    def __init__(self, capacity: int):
12        self.cap=capacity
13        self.size=0
14        self.dic={}
15        self.head=Node(-1,-1)
16        self.tail=Node(-1,-1)
17        self.head.next=self.tail
18        self.tail.prev=self.head
19
20    def detach(self, node):
21        prev_node=node.prev
22        nxt_node=node.next
23        prev_node.next=nxt_node
24        nxt_node.prev=prev_node
25
26
27    def add_to_end(self, node):
28        node.next=self.tail
29        prev_node=self.tail.prev
30        node.prev = prev_node
31        prev_node.next=node
32        self.tail.prev=node
33
34        
35        # dic 更新 ？？？
36
37    def get(self, key: int) -> int:
38        if key not in self.dic:
39            return -1
40        node=self.dic[key]
41        self.detach(node)
42        self.add_to_end(node)
43        return node.val
44
45    def put(self, key: int, value: int) -> None:
46        if key in self.dic:
47            node=self.dic[key]
48            self.detach(node)
49            node.val=value
50            self.add_to_end(node)
51        else:
52            new_node=Node(key,value)
53            # 不在，要加， 先看size
54            if self.size==self.cap:
55                #del 头
56                delete_node = self.head.next
57                self.detach(delete_node)
58                del self.dic[delete_node.key]
59                self.size-=1
60            self.add_to_end(new_node)
61            self.size+=1
62            self.dic[key]=new_node
63    
64# Your LRUCache object will be instantiated and called as such:
65# obj = LRUCache(capacity)
66# param_1 = obj.get(key)
67# obj.put(key,value)