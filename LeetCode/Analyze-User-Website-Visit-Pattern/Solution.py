1class Solution:
2    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
3        # Step 1&2: 排序后按user分组
4        data = sorted(zip(timestamp, username, website))
5        user_sites = defaultdict(list)
6        for t, u, w in data:
7            user_sites[u].append(w)
8        
9        # Step 3&4: 枚举三元组，统计不同user数
10        pattern_count = defaultdict(int)
11        for u, sites in user_sites.items():
12            seen = set()
13            for i in range(len(sites)):
14                for j in range(i+1, len(sites)):
15                    for k in range(j+1, len(sites)):
16                        pattern = (sites[i], sites[j], sites[k])
17                        if pattern not in seen:
18                            seen.add(pattern)
19                            pattern_count[pattern] += 1
20        
21        # Step 5: 取count最大、字典序最小
22        best_count = max(pattern_count.values())
23        candidates = sorted(p for p in pattern_count if pattern_count[p] == best_count)
24        return list(candidates[0])