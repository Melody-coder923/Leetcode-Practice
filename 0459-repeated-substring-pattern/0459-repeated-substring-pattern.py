class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def build_next(pattern):
            n=len(pattern)
            next=[0]*n
            j=0
            for i in range(1,n):
                while j>0 and pattern[i]!=pattern[j]:
                    j=next[j-1]
                if pattern[i]==pattern[j]:
                    j+=1
                next[i]=j
            return next
        
        n = len(s)
        next=build_next(s)
        longest=next[n-1]
        return (longest>0 and n%(n-longest)==0)


       