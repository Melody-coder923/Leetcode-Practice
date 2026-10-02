1class Solution:
2    def minEatingSpeed(self, piles: list[int], h: int) -> int:
3        # output: speed k
4        #  time h
5        #  pile<k  wait
6        #  target: finish all
7
8        n=len(piles)
9        
10        l,r=1,max(piles)+1
11
12        def can_finish(speed):
13            count=0
14            for p in piles:
15                # one time finish
16                if p<=speed:
17                    count+=1
18                #more than one time
19                else:
20                    count+=p//speed
21                    if p%speed!=0:
22                        count+=1
23            if count<=h:
24                return True
25            else:
26                return False
27        
28        while l<r: 
29            mid=(l+r)//2
30            if can_finish(mid):
31                r=mid
32            else:
33                l=mid+1
34        
35        return l
36                