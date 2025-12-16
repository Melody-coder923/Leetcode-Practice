class CustomStack:

    def __init__(self, maxSize: int):
        self.maxsize=maxSize
        self.stack=[]

    def push(self, x: int) -> None:
        if len(self.stack)!=self.maxsize:
            self.stack.append(x)
        else:
            print(f"stack still {self.stack}. Do not add another element as size is {self.maxsize}")

    def pop(self) -> int:
        if not self.stack:
            return -1
        return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.stack))):
            self.stack[i] += val
    

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)