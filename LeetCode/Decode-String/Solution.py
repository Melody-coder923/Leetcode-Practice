1class Solution:
2    def decodeString(self, s: str) -> str:
3        def dfs(i):
4            res=""
5            num=0
6            while i<len(s):
7                ch=s[i]
8                if ch.isdigit():
9                    num=num*10+ int(ch)
10                    i+=1
11                #遇到 [ 递归进去
12                elif ch=="[":
13                    inner,i=dfs(i+1)
14                    res+=num*inner
15                    num=0
16                # 遇到 ] → 当前层结束返回
17                elif ch=="]":
18                    return res,i+1
19                else:
20                    res+=ch
21                    i+=1
22            return res, i 
23            
24        ans, _ = dfs(0)
25        return ans
26                
27
28
29                
30
31