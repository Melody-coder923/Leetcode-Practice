1class Solution:
2    def predictPartyVictory(self, senate: str) -> str:
3        #NEXT ROUND
4        q1=deque() 
5        q2=deque()
6        #for senate
7        n=len(senate)
8        for idx, s in enumerate(senate):
9            if s=="R":
10                q1.append(idx)
11            else:
12                q2.append(idx)
13        
14        while q1 and q2:
15            if q1[0]<q2[0]:
16                q2.popleft()
17                nxt=q1.popleft()
18                q1.append(nxt+n)
19            else:
20                q1.popleft()
21                nxt=q2.popleft()
22                q2.append(nxt+n)
23        return "Radiant" if q1 else "Dire"
24        
25
26
27                
28            