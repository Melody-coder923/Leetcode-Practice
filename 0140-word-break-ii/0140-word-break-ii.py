class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        #139题升级版, 只要题目要“列出所有方案", 99% 会走 DFS / 回溯
        #dfs(i): 返回 s[i:] 可以构成的所有合法句子List[str] +memo
        #从字符串下标 i 开始，到字符串结尾，能组成哪些合法的句子？
        wordSet = set(wordDict)
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            #我已经刚好走到字符串末尾,这是“一条成功路径"
            if i==len(s):
                return [""]

            res = []
            for j in range(i + 1, len(s) + 1):
                word = s[i:j]
                if word in wordSet:
                    subs = dfs(j)
                    for sub in subs:
                        if sub == "":
                            res.append(word)
                        else:
                            res.append(word + " " + sub)
            memo[i] = res
            return res
        return dfs(0)
        
