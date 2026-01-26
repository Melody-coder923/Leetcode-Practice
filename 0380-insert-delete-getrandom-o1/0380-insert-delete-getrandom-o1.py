import random
class RandomizedSet:
    def __init__(self):
        self.pos={}
        self.lst=[]

    def insert(self, val: int) -> bool:
        if val not in self.pos:
            idx=len(self.lst)
            self.pos[val]=idx
            self.lst.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        else:
            idx = self.pos[val]
            last_val = self.lst[-1]

            # 把最后一个元素换到 idx
            self.lst[idx] = last_val
            self.pos[last_val] = idx

            # 删除最后一个
            self.lst.pop()
            del self.pos[val]   
            return True
        

    def getRandom(self) -> int:
        idx = random.randint(0, len(self.lst) - 1) #两边都是包含的
        return self.lst[idx]

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()