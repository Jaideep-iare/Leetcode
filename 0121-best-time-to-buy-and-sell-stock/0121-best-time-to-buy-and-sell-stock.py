class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        buy=prices[0]
        profit=0
        for i in range(n):
            if prices[i]<buy:
                buy=prices[i]
            else:
                profit=max(profit,prices[i]-buy)
        return profit