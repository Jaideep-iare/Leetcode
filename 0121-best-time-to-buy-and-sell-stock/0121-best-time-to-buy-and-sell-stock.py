class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=float("inf")
        profit=0
        for i in prices:
            if i<buy:
                buy=i
            elif buy!=i:
                profit=max(profit,i-buy)
        return profit