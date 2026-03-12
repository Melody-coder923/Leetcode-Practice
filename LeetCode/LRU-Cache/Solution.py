1class Node:
2    def __init__(self,key,value):
3        self.key=key
4        self.val=value
5        self.prev=None
6        self.next=None
7
8class LRUCache:
9# dic key-value
10# double linkedlist
11#   key    1 2
12#         node
13# head    1 2      add  ->tail (val)
14# head->old->     new tail
15    
16#      del      add
17    def __init__(self, capacity: int):
18        self.capacity=capacity #容量
19        self.size=0 # 当下
20        self.head=Node(0,0)
21        self.tail=Node(0,0)
22        self.head.next=self.tail
23        self.tail.prev=self.head
24        self.map={} # key-> node
25    
26    # speparte  
27    # size change, map not change
28    def detach(self,node):
29        prev_node=node.prev
30        next_node=node.next
31
32        prev_node.next=next_node
33        next_node.prev=prev_node
34
35        self.size-=1
36        
37
38    # add at last
39    # size change here and map not change
40    def add(self,node):
41        node.next=self.tail
42        node.prev=self.tail.prev
43
44        self.tail.prev.next=node
45        self.tail.prev=node
46
47        self.size+=1
48
49        
50    def get(self, key: int) -> int:
51        if key in self.map:
52            node=self.map[key]
53            # move the node to last
54            self.detach(node)
55            self.add(node)
56            return node.val
57        return -1
58    
59    # remember change map 
60    def put(self, key: int, value: int) -> None:
61       # if exist: find key ->update val
62        if key in self.map:
63            node=self.map[key]
64            #update vale
65            node.val=value
66            #move to last 
67            self.detach(node)
68            self.add(node)
69            
70       # if not exist -> check size(Del)-> add
71        else:
72            newNode= Node(key,value)
73            if self.size==self.capacity:
74                #delete old
75                d_node=self.head.next
76                self.detach(d_node)
77                del self.map[d_node.key]
78                # create node and add new node
79            # 不管超没超都要加
80            self.add(newNode)
81            self.map[key]=newNode
82                  
83
84# Your LRUCache object will be instantiated and called as such:
85# obj = LRUCache(capacity)
86# param_1 = obj.get(key)
87# obj.put(key,value)