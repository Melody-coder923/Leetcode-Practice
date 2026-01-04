class MyHashMap:

    def __init__(self):
        self.buckets=[[] for _ in range(1000)]
        
    def put(self, key: int, value: int) -> None:
        index=key%len(self.buckets)
        for i, (k, v) in enumerate(self.buckets[index]):
            if k == key:
                self.buckets[index][i] = (key, value)
                return
        self.buckets[index].append((key, value))

    def get(self, key: int) -> int:
        index=key%len(self.buckets)
        for k, v in self.buckets[index]:
            if k == key:
                return v
        return -1


    def remove(self, key: int) -> None:
        index=key%len(self.buckets)
        for i, (k, v) in enumerate(self.buckets[index]):
            if k == key:
                self.buckets[index].pop(i)
                return
        
        
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)