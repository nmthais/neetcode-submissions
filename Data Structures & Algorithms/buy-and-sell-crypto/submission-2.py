class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        bestBuy = prices[0]

        for sell in prices:
            profit = max(profit, sell - bestBuy)
            bestBuy = min(bestBuy, sell)

        return profit