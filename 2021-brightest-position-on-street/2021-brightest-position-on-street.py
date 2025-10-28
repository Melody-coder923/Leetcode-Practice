class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        #差分数组
        diff=defaultdict(int)
        for mid,scope in lights:
            diff[mid-scope]+=1
            diff[mid+scope+1]-=1
        
        cur=0
        maxlight=0
        maxbright=0
        for i in sorted(diff):
            cur+=diff[i]
            if cur>maxlight:
                maxlight=cur
                maxbright=i
        return maxbright

