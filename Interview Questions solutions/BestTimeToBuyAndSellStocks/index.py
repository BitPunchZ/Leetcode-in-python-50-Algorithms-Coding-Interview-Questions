class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice = float("inf")
        profit = 0

        for i, price in enumerate(prices):
            if(buyPrice > price):
                buyPrice = price
            else:
                profit = max(profit, price-buyPrice)

        return profit
