1class Solution:
2    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
3        wordDict=set(wordDict)
4        memo={}
5
6        def dfs(i):
7            if i==len(s):
8                return [""]
9            if i in memo:
10                return memo[i]
11            res=[]
12            for j in range(i+1,len(s)+1):
13                prefix=s[i:j]
14                if prefix in wordDict:
15                    tmp=dfs(j)
16                    for word in tmp:
17                        res.append((prefix+" "+word).strip())
18            memo[i]=res
19            return res
20        return dfs(0)
21                        
22                