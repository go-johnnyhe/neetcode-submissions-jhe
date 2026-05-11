class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # cheapest deal from the past I can make if I were to sell today?

        best_profit = 0
        minimum_price = float('inf')
        for price in prices:
            if price - minimum_price > best_profit:
                best_profit = price - minimum_price
            minimum_price = min(price, minimum_price)
        return best_profit