1class Codec:
2    def encode(self, strs: List[str]) -> str:
3        """Encodes a list of strings to a single string.
4        """
5        res=""
6        for word in strs:
7            num=len(word)
8            res += str(num) + "#" + word
9
10        return res
11        
12    def decode(self, s: str) -> List[str]:
13        """Decodes a single string to a list of strings.
14        """
15        i=j=0
16        res=[]
17        while i<len(s):
18            j=i
19            while s[i]!="#":
20                i+=1
21            cal=int(s[j:i])      
22            #i停留在“#”
23            res.append(s[i+1:i+1+cal])
24            i=i+1+cal
25        return res
26                
27        
28
29
30# Your Codec object will be instantiated and called as such:
31# codec = Codec()
32# codec.decode(codec.encode(strs))