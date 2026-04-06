class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_profit = float('inf')
        max_profit = 0
        for price in prices:
            min_profit = min(min_profit, price)
            max_profit = max(max_profit, price - min_profit)
        return max_profit