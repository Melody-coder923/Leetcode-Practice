1class MinStack:
2
3    def __init__(self):
4        self.min_stack=[]
5        self.stack=[]
6    
7    def push(self, val: int) -> None:
8        self.stack.append(val)
9        if not self.min_stack or val <= self.min_stack[-1]:
10            self.min_stack.append(val)
11        
12    def pop(self) -> None:
13        if not self.stack:
14            return None
15        val = self.stack.pop()
16        if val == self.min_stack[-1]:
17            self.min_stack.pop()
18        
19    def top(self) -> int:
20        if not self.stack:
21            return None
22        return self.stack[-1]
23
24    def getMin(self) -> int:
25        if not self.min_stack:
26            return None
27        return self.min_stack[-1]
28
29
30# Your MinStack object will be instantiated and called as such:
31# obj = MinStack()
32# obj.push(val)
33# obj.pop()
34# param_3 = obj.top()
35# param_4 = obj.getMin()