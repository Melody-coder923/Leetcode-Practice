1class FreqStack:
2
3    def __init__(self):
4        self.freq2group=defaultdict(list)
5        self.num2freq=defaultdict(int)
6        self.maxfreq=0
7
8    def push(self, val: int) -> None:
9        if val in self.num2freq:
10            self.num2freq[val] += 1
11            freq=self.num2freq[val]
12            self.freq2group[freq].append(val)
13        else:
14            self.num2freq[val]=1
15            freq=1
16            self.freq2group[1].append(val)
17        self.maxfreq=max(self.maxfreq,freq)
18        
19    def pop(self) -> int:
20        num=self.freq2group[self.maxfreq].pop()
21        self.num2freq[num] -= 1
22        if not self.freq2group[self.maxfreq]:
23            self.maxfreq -= 1
24        return num
25        
26
27
28# Your FreqStack object will be instantiated and called as such:
29# obj = FreqStack()
30# obj.push(val)
31# param_2 = obj.pop()