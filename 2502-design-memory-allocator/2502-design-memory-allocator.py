class Allocator:

    def __init__(self, n: int):
        self.arr=[0]*n

    def allocate(self, size: int, mID: int) -> int:
        count=0
        n = len(self.arr)
        for i in range(n):
            if self.arr[i]==0:
                count+=1
                if count==size:
                    start = i - size + 1
                    for j in range(start, start + size):
                        self.arr[j] = mID
                    return start
            else:
                count=0
        return -1
        
    def freeMemory(self, mID: int) -> int:
        free=0
        for i in range(len(self.arr)):
            if self.arr[i]==mID:
                self.arr[i]=0
                free+=1
        return free

        


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)