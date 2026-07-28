1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        profit=0
4        buyprice=prices[0]
5        for price in prices:
6            buyprice=min(price,buyprice)
7            profit=max(profit,price-buyprice)
8
9        return profit