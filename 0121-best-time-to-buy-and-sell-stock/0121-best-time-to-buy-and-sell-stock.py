class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_value = prices[0]
        for price in prices:
            if price < min_value:
                min_value = price
            else:
                profit = max(profit, price - min_value)
        return profit
