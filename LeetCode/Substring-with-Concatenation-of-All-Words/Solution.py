1class Solution:
2    def findSubstring(self, s: str, words: List[str]) -> List[int]:
3        # appear?  dict[word]=freq.  
4        # freq?    real: -freq until ==0 , match+=1,  match==len(set(words)) target
5        # slidding window left right, return left 必须一摸一样，不一样就挪动l
6        #barfoofoo barthefoo. barman
7        #012345678 9
8        #
9        #window_size=len(words)
10        n=len(s)
11        dict_target=Counter(words)
12        target=len(words)#单词个数
13        step=len(words[0]) #每个单词长度
14        l=0
15        res=[]
16        for offset in range(step):
17            l=offset
18            dict=Counter()
19            wordcount=0
20            for r in range(offset,n-step+1,step):
21                temp=s[r:r+step] #为了满足这个条件，for r 停止在n-step+1
22                if temp not in dict_target:
23                    l=r+step
24                    wordcount=0
25                    dict.clear()
26                else: #如果在目标字典
27                    dict[temp]+=1
28                    wordcount+=1
29                    # 超过频率就缩
30                    while dict_target[temp]<dict[temp]:
31                        dict[s[l:l+step]]-=1
32                        l+=step
33                        wordcount-=1
34                    if wordcount==target:
35                        res.append(l)
36                        dict[s[l:l+step]]-=1
37                        wordcount-=1
38                        l+=step
39        return res