class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # 范围船运能力: max(weight): sum(weights) 
        def can_finish(capacity, days):
            cur=0
            day=1
            for w in weights:
                if cur+w >capacity:
                    day+=1 #开启新的一天,下面清0
                    cur=0
                cur+=w
            return day<=days
         
        low,high=max(weights), sum(weights)+1 # [ )
        while low<high: # 开
            mid= (high+low)//2
            if can_finish(mid, days): 
                high=mid  # [) 
            else:
                low=mid+1
        return low
        
        



