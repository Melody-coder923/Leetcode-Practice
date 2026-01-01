class Solution:
    def maxDepth(self, s: str) -> int:
        ans,size=0,0
        for item in s:
            if item=="(":
                size+=1
            elif item==")":
                size-=1
            ans=max(ans,size)
            
        return ans