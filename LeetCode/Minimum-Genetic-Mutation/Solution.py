1class Solution:
2    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
3        bank=set(bank)
4        if startGene == endGene:
5            return 0
6
7        if endGene not in bank:
8            return -1
9        
10        n=len(startGene)
11        pattern=defaultdict(list)
12    
13        
14        for word in bank:
15            for i in range(n):
16                p=word[:i]+"*"+word[i+1:]
17                pattern[p].append(word)
18        
19        q = deque([(startGene, 0)])
20        visited={startGene}
21
22        while q:
23            word,step=q.popleft()
24            if word==endGene:
25                return step
26
27            for i in range(n):
28                p=word[:i]+"*"+word[i+1:]
29                if p in pattern:
30                    for nxt in pattern[p]:
31                        if nxt not in visited:
32                            q.append((nxt,step+1))
33                            visited.add(nxt)
34        return -1