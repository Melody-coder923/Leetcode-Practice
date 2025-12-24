class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1=l2=0
        res=[]
        n1,n2= len(word1),len(word2)
        while l1<n1 and l2<n2:
            if l1<n1:
                res.append(word1[l1])
                l1+=1
            if l2<n2:
                res.append(word2[l2])
                l2+=1
        if l1<n1:
            res.append(word1[l1:])
        if l2<n2:
            res.append(word2[l2:])

        return "".join(res)        
