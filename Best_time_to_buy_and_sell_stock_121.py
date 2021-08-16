class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value, profit = prices[0], 0
        for price in prices:
            if price < min_value:
                min_value = price
            else:
                profit = max(profit, price-min_value)
        return profit

