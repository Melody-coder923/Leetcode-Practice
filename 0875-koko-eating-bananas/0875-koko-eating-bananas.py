class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canfinish(k):
            hour=0
            for pile in piles:   
                hour += pile // k
                if pile % k > 0:
                    hour += 1
            return hour <= h

        n=len(piles)
        r=max(piles)+1#最多吃多少根
        l=1
        while l<r:
            mid=l+(r-l)//2 #1, 12 ->mid=7, 4 , 2, 3
            if canfinish(mid):
                r=mid  #r=7 r=4 
            else:
                l=mid+1 # l=3, 4
        return l



             


