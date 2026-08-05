1class Solution:
2    def minimumPushes(self, word: str) -> int:
3        n=len(word)
4        if n<=8:
5            return n
6
7        total=0
8        level=1
9        while n!=0:
10            cur_count=min(8,n)
11            total+=cur_count*level
12            level+=1
13            n=n-cur_count
14
15        return total
16