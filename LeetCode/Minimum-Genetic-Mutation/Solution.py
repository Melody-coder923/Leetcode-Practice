1class Solution:
2    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
3        bank=set(bank)
4
5        if endGene not in bank:
6            return -1
7        
8        n=len(startGene)
9        pattern=defaultdict(list)
10    
11        
12        for word in bank:
13            for i in range(n):
14                p=word[:i]+"*"+word[i+1:]
15                pattern[p].append(word)
16        
17        q = deque([(startGene, 0)])
18        
19        visited={startGene}
20        while q:
21            curr,step=q.popleft()
22            if curr==endGene:
23                return step
24            for i in range(n):
25                compare=curr[:i]+"*"+curr[i+1:]
26                if compare in pattern:
27                    for nxt in pattern[compare]:
28                        if nxt not in visited:
29                            q.append((nxt,step+1))
30                            visited.add(nxt)
31        return -1
32
33            
34