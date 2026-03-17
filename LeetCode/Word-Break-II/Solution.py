1class Solution:
2    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
3        #139题升级版, 只要题目要“列出所有方案", 99% 会走 DFS / 回溯
4        #dfs(i): 返回 s[i:] 可以构成的所有合法句子List[str] +memo
5        #从字符串下标 i 开始，到字符串结尾，能组成哪些合法的句子？
6        wordSet = set(wordDict)
7        memo = {}
8        def dfs(i):
9            if i in memo:
10                return memo[i]
11            #我已经刚好走到字符串末尾,这是“一条成功路径"
12            if i==len(s):
13                return [""]
14
15            res = []
16            for j in range(i + 1, len(s) + 1):
17                word = s[i:j]
18                if word in wordSet:
19                    subs = dfs(j)
20                    for sub in subs:
21                        if sub == "":
22                            res.append(word)
23                        else:
24                            res.append(word + " " + sub)
25                        #隐式回溯:如果凑不上, 选择会被忽略,没有任何东西加入res
26            memo[i] = res
27            return res
28        return dfs(0)
29        
30