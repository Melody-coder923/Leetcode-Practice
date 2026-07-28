1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        buyprice= prices[0]
4        profit=0
5        for price in prices:
6            if price>buyprice:
7                newprofit= price-buyprice
8                if newprofit>profit:
9                    profit=newprofit
10            else:
11                buyprice=price
12        return(profit)