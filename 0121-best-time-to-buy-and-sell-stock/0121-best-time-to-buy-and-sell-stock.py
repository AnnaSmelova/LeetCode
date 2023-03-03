class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value = float('inf')
        profit = 0
        for p in prices:
            if p < min_value:
                min_value = p
            elif profit < p - min_value:
                profit = p - min_value
        return profit
