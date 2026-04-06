class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 10 1 5 6 7 1
        #    l     r
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            min_price = min(price, min_price)
            if max_profit < price - min_price:
                max_profit = price - min_price
        return max_profit