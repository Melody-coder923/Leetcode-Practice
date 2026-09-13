1class Solution:
2    def findAnagrams(self, s: str, p: str) -> List[int]:
3        m,n=len(s),len(p)
4        if m<n:
5            return []
6        
7        target=[0]*26
8        window=[0]*26
9
10        for char in p:
11            target[ord(char)-ord("a")]+=1
12        
13        res=[]
14    
15        for r in range(m):
16            window[ord(s[r]) - ord('a')] += 1
17
18            if r >= n:
19                window[ord(s[r - n]) - ord('a')] -= 1
20
21            # 窗口长度达到 k
22            if r >= n - 1 and window == target:
23                res.append(r - n + 1)
24
25        return res