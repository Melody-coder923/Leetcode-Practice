1class MinStack:
2
3    def __init__(self):
4        self.stack=[]
5        self.minstack=[]
6
7    def push(self, value: int) -> None:
8        self.stack.append(value)
9        if not self.minstack or value <= self.minstack[-1]:
10            self.minstack.append(value)
11        
12
13    def pop(self) -> None:
14        if self.stack:
15            val=self.stack.pop()
16            if self.minstack and val ==self.minstack[-1]:
17                self.minstack.pop()
18
19    def top(self) -> int:
20        if self.stack:
21            return self.stack[-1]
22        
23
24    def getMin(self) -> int:
25        if self.minstack:
26            return self.minstack[-1]
27
28
29# Your MinStack object will be instantiated and called as such:
30# obj = MinStack()
31# obj.push(value)
32# obj.pop()
33# param_3 = obj.top()
34# param_4 = obj.getMin()