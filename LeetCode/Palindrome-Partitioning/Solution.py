1class Solution:
2    def partition(self, s: str) -> List[List[str]]:
3        def is_Panlindrom(s,l,r):
4            while l<r:
5                if s[l]!=s[r]:
6                    return False
7                l+=1
8                r-=1
9            return True
10        res=[]
11        def backtrack(path,i):
12            if i==len(s):
13                res.append(path[:])
14                return 
15            for j in range(i,len(s)):
16                if is_Panlindrom(s,i,j):
17                    path.append(s[i:j+1])
18                    backtrack(path,j+1)
19                    path.pop()
20        backtrack([],0)
21        return res