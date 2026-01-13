class Solution:
    def reverseWords(self, s: str) -> str:
        res=[]
        i,n=0,len(s)
        while i < n:
            if s[i]!=" ":
                start=i
                while i<n and s[i]!=" ":
                    i+=1
                res.append(s[start:i])    
            else:
                i+=1
        return " ".join(res[::-1])