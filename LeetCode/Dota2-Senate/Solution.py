1class Solution:
2    def predictPartyVictory(self, senate: str) -> str:
3        n = len(senate)
4        # 1. 初始入队：分别记录两个阵营议员的原始下标
5        radiant = deque()
6        dire = deque()
7        
8        for i, s in enumerate(senate):
9            if s == 'R':
10                radiant.append(i)
11            else:
12                dire.append(i)
13        
14        # 2. 模拟投票过程
15        # 只要两个队列都不为空，说明斗争还在继续
16        while radiant and dire:
17            r_idx = radiant.popleft()
18            d_idx = dire.popleft()
19            
20            # 谁的下标小，谁就先行使权利（禁言对方）
21            if r_idx < d_idx:
22                # Radiant 先手，禁言掉当前的 Dire
23                # Radiant 议员获得进入下一轮的机会，下标更新为 i + n
24                radiant.append(r_idx + n)
25            else:
26                # Dire 先手，禁言掉当前的 Radiant
27                # Dire 议员获得进入下一轮的机会，下标更新为 i + n
28                dire.append(d_idx + n)
29        
30        # 3. 宣布胜利：哪个队列还有人，哪方就赢了
31        return "Radiant" if radiant else "Dire"