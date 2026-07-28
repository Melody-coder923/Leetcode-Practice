1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        buyprice=prices[0]
4        profit=0
5
6        for price in prices:
7            buyprice=min(price,buyprice)
8            profit=max(profit, price-buyprice)
9        
10        return profit